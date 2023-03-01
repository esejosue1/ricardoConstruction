
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('quote/', include("quote.urls")),
    path('projects/', include('projects.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

