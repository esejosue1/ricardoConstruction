from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

from .form import QuoteForm
from .models import Quote

import datetime

# Create your views here.
def quote(request):
    
    if request.method == "POST":
        form=QuoteForm(request.POST)
        if form.is_valid():
            data= Quote()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.message = form.cleaned_data['message']
            data.save()
            messages.success(request, 'Contact request submitted successfully.')

            #receive the email
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            message=request.POST['message']

            send_mail(
                'Message from ' + first_name,
                message,
                email,
                ['josuegallardolara1@gmail.com'],
            )
        else:
            messages.error(request, 'Invalid form submission.')

    return render(request, "quote/quote.html")

def getQuote(request):
    if request.method == "POST":
        form=QuoteForm(request.POST)
        if form.is_valid():
            print('valid')
    form = QuoteForm()
    return render(request,"quote/quote.html", {'form':form} )