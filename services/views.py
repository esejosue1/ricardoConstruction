from django.shortcuts import render
from django.http import HttpResponse
from .models import Services

# Create your views here.
def services(request):

    services=Services.objects.all()

    context={
        'services':services,
    }

    return render(request, "services/services.html", context)


def serviceDetail(request, slug_detail):
    q=Services.objects.filter(slug=slug_detail)
    if q.exists():
        q=q.first()
    else:
        return HttpResponse("<h1>Page not found </h1>")
    
    context={
        'services':q
    }
    return render(request, 'services/service-details.html', context)