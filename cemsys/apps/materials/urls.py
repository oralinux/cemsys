"""define materials urls"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'materials/$', views.material_purchase, name='materials'),

    # 进货
    url(r'new_material/$', views.new_material, name='new_material'),

    # 材料信息列表
    url(r'list_material/$', views.list_materials, name='list_material'),
    url(r'test_material/$', views.list_materials, name='test_material'),

    # 材料信息修改
    url(r'update_material/$', views.update_materials, name='update_material'),

    # 删除材料信息
    url(r'del_material/$', views.delete_materials, name='del_material'),
]
