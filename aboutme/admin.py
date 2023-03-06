from django.contrib import admin
from .models import Employees, CompanyInfo

# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'title')

class CompanyInfoAdmin(admin.ModelAdmin):
    list_display=('company_name','address')

admin.site.register(Employees, EmployeesAdmin)
admin.site.register(CompanyInfo, CompanyInfoAdmin)