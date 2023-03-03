from django.contrib import admin
from .models import Employees

# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'title')

admin.site.register(Employees, EmployeesAdmin)