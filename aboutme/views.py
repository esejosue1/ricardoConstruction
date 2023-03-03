from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees

# Create your views here.
def story(request):
    employees=Employees.objects.all()

    context={
        'employees':employees
    }
    return render(request, 'story/about.html', context)