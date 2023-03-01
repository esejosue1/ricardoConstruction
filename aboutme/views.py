from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def story(request):
    return render(request, 'story/about.html')