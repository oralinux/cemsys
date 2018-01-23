from django import forms
from cemsys.apps.users.models import Person


class UserAddForm(forms.Form):
    """创建新用户"""
    sex = forms.CharField(label='sex', max_length=1)
    age = forms.IntegerField(required=False)
    born_date = forms.DateField()
    address = forms.Textarea()
    work_unit = forms.CharField(max_length=100, required=False)
    phone = forms.IntegerField()
    contact = forms.CharField(max_length=17, required=False)
    introduce = forms.Textarea()

    class Meta:
        model = Person
        fields = ('username', 'password1', 'password2', 'email', 'sex', 'age'
                  , 'born_date', 'address', 'work_unit', 'phone', 'contact',
                  'introduce')

    # 判断年龄是否为负数
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 1:
            raise forms.ValidationError("年龄不能小于1岁")
        return age

    # 判断email是否已经存在
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            Person.get(email=email)
        except Person.DoesNotExist:
            return email
        raise forms.ValidationError("Email已经存在，请更换其它email地址", code="重复邮件地址")

    # 保存信息
    def save(self, commit=True):
        user = super(UserAddForm, self).save(commit=False)
        user.sex = self.cleaned_data['sex']
        user.age = self.cleaned_data['age']
        user.born_date = self.cleaned_data['born_date']
        user.address = self.cleaned_data['address']
        user.work_unit = self.cleaned_data['work_unit']
        user.phone = self.cleaned_data['phone']
        user.contact = self.cleaned_data['contact']
        user.introduce = self.cleaned_data['introduce']

        if commit:
            user.save()
        return user
