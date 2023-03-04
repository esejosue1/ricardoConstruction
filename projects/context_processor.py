from os import link
from sre_constants import CATEGORY
from .models import Projects

def globalProjects(request):
    gloabal_projects=Projects.objects.all()

    return dict(gloabal_projects=gloabal_projects)