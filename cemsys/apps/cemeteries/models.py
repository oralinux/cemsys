from django.db import models


# Create your models here.
class Grave(models.Model):
    """定义墓穴状态"""
    grave_code = models.CharField(max_length=6)
    grave_type = models.CharField(max_length=12)
    grave_status = models.CharField(max_length=10)
    grave_pic = models.ImageField(upload_to='images')
    picture_name = models.CharField(max_length=20, default='%Y%m%d.jpg')

    def __str__(self):
        return self.grave_code


class Area(models.Model):
    """定义墓区"""
    area_code = models.CharField(max_length=10)
    area_name = models.CharField(max_length=20)
    remark = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    operator = models.CharField(max_length=12)
    modify_date = models.DateTimeField(auto_now=True)
    modify_user = models.CharField(max_length=12, default='')

    def __str__(self):
        return self.area_code


class Cate(models.Model):
    """定义墓型的分类"""
    SINGLE = '单'
    DOUBLE = '双'
    THREE = '多人墓'
    CATE_IN_CHOICES = (
        (SINGLE, '单墓'),
        (DOUBLE, '双墓'),
        (THREE, '多人墓')
    )
    cate_code = models.CharField(max_length=10)
    cate_name = models.CharField(max_length=20)
    cate_type = models.CharField(
        max_length=4,
        choices=CATE_IN_CHOICES,
        default=SINGLE
    )
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    modify_date = models.DateTimeField(auto_now_add=True)
    modify_user = models.CharField(max_length=12, default='')

    def __str__(self):
        return self.cate_code


class Tomb(models.Model):
    """定义墓位"""

    area_code = models.CharField(max_length=10)
    area_name = models.CharField(max_length=20)
    cate_code = models.CharField(max_length=10)
    cate_name = models.CharField(max_length=20)
    cate_type = models.CharField(max_length=4)
    grave_code = models.CharField(max_length=6)
    grave_status = models.CharField(max_length=10)
    tomb_row = models.CharField(max_length=4)
    tomb_col = models.CharField(max_length=4)
    tomb_attach = models.CharField(max_length=4, default=0)
    area = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    operator = models.CharField(max_length=12)

    def __str__(self):
        return self.tomb_row + '排' + self.tomb_col + '号'
