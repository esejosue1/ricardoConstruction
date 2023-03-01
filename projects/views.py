from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects

# Create your views here.
def projects(request):
    projects=Projects.objects.all()

    context={
        'projects':projects
    }
    return render(request, 'jobs/projects.html', context)