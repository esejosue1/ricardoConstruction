from os import link
from sre_constants import CATEGORY
from .models import Category

def category_links(request):
    links = Category.objects.all()
    return dict(links=links)