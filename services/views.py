from django.shortcuts import render
from .models import Services

# Create your views here.
def services(request):

    services=Services.objects.all()

    context={
        'services':services,
    }

    return render(request, "services/services.html", context)


def serviceDetail(request):
    return render(request, 'services/service-details.html')