from django.shortcuts import render, HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from cemsys.apps.cemeteries.models import Grave, Area, Cate, Tomb
from django.contrib.auth.decorators import login_required
import json
import time
from cemsys.apps.admins.encode import DecimalEncoder


# Create your views here.
@login_required
def cemeteries(request):
    """墓区设置"""

    return render(request, 'cemeteries/index.html')


@login_required
def list_areas(request):
    """墓区详细信息"""
    records = Area.objects.values('id', 'area_code', 'area_name', 'remark', 'create_date', 'operator',
                                  'modify_date', 'modify_user')

    data = json.dumps(list(records), ensure_ascii=False, cls=DecimalEncoder)

    return HttpResponse(data)


@login_required
def new_areas(request):
    """新增墓区"""
    if request.method == 'POST':
        area_code = request.POST['area_code']
        area_name = request.POST['area_name']
        remark = request.POST['remark']
        operator = request.POST['operator']

        Area.objects.create(area_code=area_code, area_name=area_name, remark=remark,
                            operator=operator)

    return HttpResponseRedirect(reverse('cemeteries:cemeteries'))


@login_required
def update_areas(request):
    """修改墓区信息"""
    if request.method == 'POST':
        area_id = request.POST['area_id']
        area_name = request.POST['area_name']
        remark = request.POST['remark']
        modify_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        modify_user = request.POST['modify_user']

        Area.objects.filter(id=area_id).update(area_name=area_name, remark=remark, modify_date=modify_date,
                                               modify_user=modify_user)

    return HttpResponseRedirect(reverse('cemeteries:cemeteries'))


@login_required
def delete_areas(request):
    """删除墓区信息"""
    if request.method == 'POST':
        area_id = request.POST['area_id']

        area = Area.objects.get(id=area_id)
        area.delete()

    return HttpResponseRedirect(reverse('cemeteries:cemeteries'))


@login_required
def graves(request):
    """墓区设置"""

    return render(request, 'cemeteries/grave_status.html')


@login_required
def list_graves(request):
    """显示墓穴状态"""

    records = Grave.objects.values('id', 'grave_code', 'grave_type', 'grave_status', 'grave_pic')

    data = json.dumps(list(records), ensure_ascii=False)

    return HttpResponse(data)


@login_required
def new_graves(request):
    """新增墓穴状态"""

    if request.method == 'POST':
        new_status = Grave(
            grave_code=request.POST.get('grave_code'),
            grave_type=request.POST.get('grave_type'),
            grave_status=request.POST.get('grave_status'),
            grave_pic=request.FILES.get('grave_pic'),
            picture_name=request.FILES.get('grave_pic').name
        )

        new_status.save()

    return HttpResponseRedirect(reverse('cemeteries:cemeteries'))


@login_required
def update_graves(request):
    """修改墓穴状态信息"""

    if request.method == 'POST':
        grave_id = request.POST['grave_id']
        grave_code = request.POST['grave_code']
        grave_type = request.POST['grave_type']
        grave_status = request.POST['grave_status']

        Grave.objects.filter(id=grave_id).update(grave_code=grave_code, grave_type=grave_type, grave_status=grave_status)

    return HttpResponseRedirect(reverse('cemeteries:cemeteries'))


@login_required
def delete_graves(request):
    """删除墓穴状态信息"""

    if request.method == 'POST':
        grave_id = request.POST['grave_id']

        grave = Grave.objects.get(id=grave_id)
        grave.delete()

    return HttpResponseRedirect(reverse('cemeteries:cemeteries'))


@login_required
def cates(request):
    """墓区设置"""

    return render(request, 'cemeteries/cate.html')


@login_required
def list_cates(request):
    """显示墓型"""

    records = Cate.objects.values('id', 'cate_code', 'cate_name', 'cate_type', 'length', 'width', 'height'
                                  , 'modify_date', 'modify_user')

    data = json.dumps(list(records), ensure_ascii=False, cls=DecimalEncoder)

    return HttpResponse(data)


@login_required
def new_cates(request):
    """新增墓穴状态"""

    if request.method == 'POST':
        new_cate = Cate(
            cate_code=request.POST.get('cate_code'),
            cate_name=request.POST.get('cate_name'),
            cate_type=request.POST.get('cate_type'),
            length=request.POST.get('length'),
            width=request.POST.get('wide'),
            height=request.POST.get('deep'),
            modify_user=request.POST.get('modify_user'),
        )

        new_cate.save()

    return HttpResponseRedirect(reverse('cemeteries:cates'))


@login_required
def update_cates(request):
    """修改墓穴状态信息"""

    if request.method == 'POST':
        cate_id = request.POST['cate_id']
        cate_name = request.POST['cate_name']
        cate_type = request.POST['cate_type']
        length = request.POST['length']
        width = request.POST['wide']
        height = request.POST['deep']
        modify_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        modify_user = request.POST['modify_user']

        Cate.objects.filter(id=cate_id).update(cate_name=cate_name, cate_type=cate_type, length=length,
                                               width=width, height=height, modify_date=modify_date
                                               , modify_user=modify_user)

    return HttpResponseRedirect(reverse('cemeteries:cates'))


@login_required
def delete_cates(request):
    """删除墓穴状态信息"""

    if request.method == 'POST':
        cate_id = request.POST['cate_id']

        cate = Cate.objects.get(id=cate_id)
        cate.delete()

    return HttpResponseRedirect(reverse('cemeteries:cates'))


# 墓位设置
@login_required
def tombs(request):
    """墓位管理"""

    return render(request, 'cemeteries/tomb.html')


@login_required
def list_tombs(request):
    """墓位列表"""

    # 获取墓型列表：墓型编号、名称、面积
    tomb = Tomb.objects.values('id', 'area_code', 'area_name', 'cate_code', 'cate_name'
                               , 'cate_type', 'grave_status', 'tomb_row', 'tomb_col', 'tomb_attach'
                               , 'area', 'create_date', 'operator')

    data = json.dumps(list(tomb), ensure_ascii=False, cls=DecimalEncoder)

    return HttpResponse(data)


@login_required
def get_catetype_list(request, cate_name):
    """获取墓型对应的类型(单、双墓等)"""

    if request.method == 'POST':
        categories = Cate.objects.filter(cate_name=cate_name).values('id', 'cate_type', 'cate_code', 'length', 'width', 'height')

        return HttpResponse(json.dumps(list(categories)))
    else:
        raise Http404


@login_required
def get_area_list(request, area_name):
    """获取墓型编号"""
    if request.method == 'POST':
        area = Area.objects.filter(area_name=area_name).values('id', 'area_code', 'area_name')

        return HttpResponse(json.dumps(list(area)))
    else:
        return Http404


@login_required
def new_tombs(request):
    """单个墓位新增"""

    if request.method == 'POST':
        new_tomb = Tomb(
            area_code=request.POST.get('area_code'),
            area_name=request.POST.get('area_name'),
            cate_code=request.POST.get('cate_code'),
            cate_name=request.POST.get('cate_name'),
            cate_type=request.POST.get('cate_type'),
            grave_code=request.POST.get('grave_code'),
            grave_status=request.POST.get('grave_status'),
            tomb_row=request.POST.get('tomb_row'),
            tomb_col=request.POST.get('tomb_col'),
            tomb_attach=request.POST.get('tomb_attach'),
            area=request.POST.get('area'),
            create_date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
            operator=request.POST.get('operator')
        )

        new_tomb.save()

    return HttpResponseRedirect(reverse('cemeteries:tombs'))


@login_required
def bulk_new_tombs(request):
    """批量新增墓位"""

    if request.method == 'POST':
        area_code = request.POST['area_code']
        area_name = request.POST['area_name']
        cate_code = request.POST['cate_code']
        cate_name = request.POST['cate_name']
        cate_type = request.POST['cate_type']
        grave_code = request.POST['grave_code']
        grave_status = request.POST['grave_status']
        tomb_attach = request.POST['tomb_attach']
        area = request.POST['area'],
        create_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        operator = request.POST['operator']
        tomb_rows = int(request.POST['tomb_rows'])
        tomb_cols = int(request.POST['tomb_cols'])
        tomb_list = []
        for row in range(1, tomb_rows):
            for col in range(1, tomb_cols):
                tomb_list.append(Tomb(area_code=area_code, area_name=area_name, cate_code=cate_code
                                      , cate_name=cate_name, cate_type=cate_type, grave_code=grave_code
                                      , grave_status=grave_status, tomb_row=row, tomb_col=col
                                      , tomb_attach=tomb_attach, area=area, create_date=create_date
                                      , operator=operator))

        Tomb.objects.bulk_create(tomb_list)

    return HttpResponseRedirect(reverse('cemeteries:tombs'))


@login_required
def update_tombs(request):
    """修改墓位"""

    if request.method == 'POST':
        return True

    return HttpResponseRedirect(reverse('cemeteries:tombs'))


@login_required
def delete_tombs(request):
    """删除墓位"""

    if request.method == 'POST':
        return True

    return HttpResponseRedirect(reverse('cemeteries:tombs'))


@login_required
def bulk_delete_tombs(request):
    """批量删除墓位"""

    if request.method == 'POST':
        return True

    return HttpResponseRedirect(reverse('cemeteries:tombs'))
