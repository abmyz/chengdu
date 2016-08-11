from django.shortcuts import render
from django.shortcuts import render_to_response
from kid.models import Qingyang
def map(request):
    list = Qingyang.objects.all()
    return render_to_response('baidu.html', {'point_list':list})
