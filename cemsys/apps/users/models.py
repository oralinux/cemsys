from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Person(User):
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    born_date = models.DateField()
    address = models.TextField()
    work_unit = models.CharField(max_length=100)
    phone = models.IntegerField()
    contact = models.CharField(max_length=17)
    introduce = models.TextField()

    class Meta(User.Meta):
        db_table = 'person'

