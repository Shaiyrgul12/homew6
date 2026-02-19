from django.contrib import admin
from apps.student.models import MyInfo, CompanyInfo 


# Register your models here.

admin.site.register(MyInfo)
admin.site.register(CompanyInfo)
