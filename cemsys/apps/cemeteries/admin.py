from django.contrib import admin
from .models import Grave, Tomb, Cate, Area


# Register your models here.
@admin.register(Grave)
class GraveAdmin(admin.ModelAdmin):
    pass


@admin.register(Tomb)
class TombAdmin(admin.ModelAdmin):
    pass


@admin.register(Cate)
class CateAdmin(admin.ModelAdmin):
    pass


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('area_code', 'area_name', 'remark', 'operator', 'create_date')

