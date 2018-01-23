from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
import json
from .forms import UserAddForm


# Create user manage views here.
@login_required
def user_manage(request):
    """user management"""
    return render(request, 'admins/users.html')


@login_required
def user_add(request):
    """add user"""
    return render(request, 'admins/user_add.html')


@login_required
def user_list(request):
    """用户列表"""
    return render(request, 'admins/test.html')


def list_data():
    """测试使用"""
    for i in range(1, 51):
        yield {
            'id': i,
            'name': "测试 " + str(i),
            'price': '描述'
        }


@login_required
def list_users(request):
    """返回数据"""
    records = []
    for record in list_data():
        records.append(record)

    data = json.dumps(records, ensure_ascii=False)
    return HttpResponse(data)

#
# @login_required
# def new_user(request):
#     """创建新用户"""
#
#     if request.method != 'POST':
#         form = UserAddForm()
#     else:
#         form = UserAddForm(request.POST)
#         if form.is_valid():
#             new_user = form.save(commit=False)
#     context = {'user': form}
#     return render(request, context)
