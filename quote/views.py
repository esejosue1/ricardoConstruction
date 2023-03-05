from django.shortcuts import render

from django.core.mail import send_mail

from .form import QuoteForm
from .models import Quote

import datetime



def contact(request):
    return render(request, 'quote/contact.html')

def getQuote(request):
    if request.method == "POST":
        form=QuoteForm(request.POST)
        if form.is_valid():
            print('valid')
    form = QuoteForm()
    return render(request,"quote/quote.html", {'form':form} )