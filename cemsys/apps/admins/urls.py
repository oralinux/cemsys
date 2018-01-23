"""define admin urls"""
from django.conf.urls import url
from . import views, users

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'user_manage/$', users.user_manage, name='user_manage'),

    url(r'statistic/$', views.statistics, name='statistics'),

    url(r'user_add/$', users.user_add, name='user_add'),

    url(r'user_list/$', users.user_list, name='user_list'),

    url(r'show_user/$', users.list_users, name='show_user')
]
