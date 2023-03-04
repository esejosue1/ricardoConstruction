from os import link
from sre_constants import CATEGORY
from .models import Services

def service_links(request):
    service_links = Services.objects.all()
    return dict(service_links=service_links)