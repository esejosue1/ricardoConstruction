from os import link
from sre_constants import CATEGORY
from .models import CompanyInfo

def about_me_links(request):
    links = CompanyInfo.objects.all()
    return dict(about_me=links)