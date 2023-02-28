from django.contrib import admin
from .models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display=['created_at',"first_name","last_name", "phone", "message"]

# Register your models here.
admin.site.register(Quote, QuoteAdmin)