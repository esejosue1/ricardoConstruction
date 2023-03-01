from django.contrib import admin
from .models import Projects


class AdminProjects(admin.ModelAdmin):
    list_display=("project_title", "project_category", 'project_client', "project_date")

# Register your models here.
admin.site.register(Projects, AdminProjects)