from django.shortcuts import render
from my_app.models import Service

def service_view(request):

    obj = Service.objects.all()

    context = {
        'obj':obj,
    }
    return render(request,'service.html',context)


def detail_view(request,slug):

    obj1 = Service.objects.get(slug=slug)

    context = {
    'obj1':obj1
    }
    return render(request,'service-detail.html',context)



