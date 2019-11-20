from django.shortcuts import render,HttpResponse
from cmdb.models import Asset
from  django.views import View
from django.http import JsonResponse
from django.db.models import Count

def index(request):
    return render(request,'index.html')


#### 数据可视化
class DashView(View):
    def get(self, request):
        l1 = ['类型\状态']
        li = []
        device_type = dict(Asset.device_type_choices)
        device_status = dict(Asset.device_status_choices)
        for x in list(device_status.keys()):
            status_qs = dict(Asset.objects.filter(device_status_id=x).values_list('device_status_id').annotate(value=Count('device_status_id')))
            if status_qs:
                l1.append(device_status.get(x))
            else:
                device_status.pop(x) 
        li.append(l1)
        for j in device_status.keys():
            type_qs = dict(Asset.objects.filter(device_type_id=j).values_list('device_status_id').annotate(value=Count('device_status_id')))
            type_qs = list(type_qs.values())
            type_qs.insert(0,device_type.get(j))
            li.append(type_qs)
            print(li)
        return JsonResponse(li, safe=False)