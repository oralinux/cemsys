# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# login the system
def login_in(request):
    """login the system"""
    return render(request, 'logins/login.html')


def login_view(request):
    """login validate"""
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect(reverse('admins:index'))
    else:
        return "User not exists"


def logout_view(request):
    """logout"""
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
