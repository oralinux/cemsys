"""define cemeteries urls"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'cemeteries/$', views.cemeteries, name='cemeteries'),

    # 墓区设置相关操作
    # 列出相应墓区信息
    url(r'list_area/$', views.list_areas, name='list_area'),

    # 新增墓区信息
    url(r'new_area/$', views.new_areas, name='new_area'),
    # 修改墓区信息
    url(r'update_area/$', views.update_areas, name='update_area'),
    # 删除墓区信息
    url(r'delete_area/$', views.delete_areas, name='delete_area'),

    # 墓穴状态相关处理操作
    url(r'graves/$', views.graves, name="graves"),
    url(r'list_grave/$', views.list_graves, name='list_grave'),

    # 新增
    url(r'new_grave/$', views.new_graves, name='new_grave'),

    # 修改墓穴信息
    url(r'update_grave/$', views.update_graves, name='update_grave'),

    # 删除墓穴信息
    url(r'delete_grave/$', views.delete_graves, name='delete_grave'),

    # 墓型相关操作
    url(r'cates/$', views.cates, name='cates'),
    url(r'list_cate/$', views.list_cates, name='list_cate'),
    url(r'getTypeList/(?P<cate_name>\w+)/$', views.get_catetype_list, name='getTypeList'),
    url(r'getAreaCode/(?P<area_name>\w+)/$', views.get_area_list, name='getAreaCode'),

    # 新增
    url(r'new_cate/$', views.new_cates, name='new_cate'),

    # 修改墓型信息
    url(r'update_cate/$', views.update_cates, name='update_cate'),

    # 删除墓型信息
    url(r'delete_cate/$', views.delete_cates, name='delete_cate'),

    # 墓位管理
    url(r'tombs/$', views.tombs, name='tombs'),
    url(r'list_tomb/$', views.list_tombs, name='list_tomb'),

    # 单条新增墓位
    url(r'new_tomb/$', views.new_tombs, name='new_tomb'),

    # 批量新增墓位
    url(r'bulk_new_tomb/$', views.bulk_new_tombs, name='bulk_new_tomb'),

    # 更新墓位
    url(r'update_tomb/$', views.update_tombs, name='update_tomb'),
    # 删除墓位
    url(r'delete_tomb/$', views.delete_tombs, name='delete_tomb'),

    # 批量删除墓位
    url(r'bulk_delete_tomb/$', views.bulk_delete_tombs, name='bulk_delete_tomb'),

]
