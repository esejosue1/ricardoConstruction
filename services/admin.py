from django.contrib import admin
from .models import Services

class ServicesAdmin(admin.ModelAdmin):
    list_display=('title', 'introduction')

# Register your models here.
admin.site.register(Services, ServicesAdmin)