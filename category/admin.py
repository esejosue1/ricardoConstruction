from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('job_category',)}
    list_display = ('job_category', 'slug')

# Register your models here.
admin.site.register(Category, CategoryAdmin)