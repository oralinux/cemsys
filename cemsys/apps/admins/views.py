from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import json


# Create your views here.
@login_required
def index(request):
    """homepage"""
    return render(request, 'admins/index.html')


@login_required
def receipt_material(request):
    """receipt material """
    return HttpResponseRedirect(reverse('admins:index'))


@login_required
def statistics(request):
    """data statistics"""
    return render(request, 'admins/statistics.html')
