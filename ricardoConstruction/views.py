from django.shortcuts import render
from django.contrib import messages

from quote.models import Quote
from quote.form import QuoteForm

def home(request):
    return render(request,'index.html')

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

            
        else:
            messages.error(request, 'Invalid form submission.')

    return render(request, "quote/quote.html")
