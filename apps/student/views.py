from django.shortcuts import render
from apps.student.models import MyInfo, CompanyInfo

# Create your views here.
def base_view(request):
    info=MyInfo.objects.first()
    return render(request, 'base.html', locals())

def homepage_view(request):
    return render(request, 'homepage.html', locals())

def urmat_view(request):
    company=CompanyInfo.objects.first()
    return render(request, 'urmat.html', locals())

def sierra_view (request):
    company=CompanyInfo.objects.first()
    return render(request, 'sierra.html', locals())