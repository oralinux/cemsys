from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import json
from cemsys.apps.materials.models import Material
from cemsys.apps.admins.encode import DecimalEncoder


# Create your views here.
@login_required
def list_materials(request):
    """获取材料信息"""

    records = Material.objects.values('id', 'mater_code', 'mater_name', 'mater_model',
                                      'receipt_price', 'receipt_count', 'receipt_date', 'operator')

    data = json.dumps(list(records), ensure_ascii=False, cls=DecimalEncoder)

    return HttpResponse(data)


@login_required
def delete_materials(request):
    """删除材料信息"""

    if request.method == 'POST':
        mater_id = request.POST['mater_id']
        material = Material.objects.get(id=mater_id)
        material.delete()

    return HttpResponseRedirect(reverse('materials:materials'))


@login_required
def update_materials(request):
    """修改材料信息"""

    if request.method == 'POST':
        mater_id = request.POST['mater_id']
        mater_code = request.POST['mater_code']
        mater_name = request.POST['mater_name']
        mater_model = request.POST['mater_model']
        receipt_price = request.POST['receipt_price']
        receipt_count = request.POST['receipt_count']
        receipt_date = request.POST['receipt_date']
        operator = request.POST['operator']

        Material.objects.filter(id=mater_id).update(mater_code=mater_code, mater_name=mater_name,
                                                    mater_model=mater_model, receipt_price=receipt_price,
                                                    receipt_count=receipt_count, receipt_date=receipt_date, operator=operator)

    return HttpResponseRedirect(reverse('materials:materials'))


@login_required
def new_material(request):
    """新增材料信息"""
    if request.method == 'POST':
        mater_code = request.POST['mater_code']
        mater_name = request.POST['mater_name']
        mater_model = request.POST['mater_model']
        receipt_price = request.POST['receipt_price']
        receipt_count = request.POST['receipt_count']
        receipt_date = request.POST['receipt_date']
        operator = request.POST['operator']

        Material.objects.create(mater_code=mater_code, mater_name=mater_name, mater_model=mater_model,
                                receipt_price=receipt_price, receipt_count=receipt_count,
                                receipt_date=receipt_date, operator=operator)

    return HttpResponseRedirect(reverse('materials:materials'))


@login_required
def material_purchase(request):
    """材料采购"""

    return render(request, 'materials/index.html')
