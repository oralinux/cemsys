"""define admin urls"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.login_in, name='login'),

    # login view
    url(r'login_view/$', views.login_view, name='login_view'),

    # logout
    url(r'logout/$', views.logout_view, name='logout'),

]
