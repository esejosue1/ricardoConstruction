from django.shortcuts import render
from .form import QuoteForm
from .models import Quote

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
    return render(request, "quote/quote.html")

def getQuote(request):
    if request.method == "POST":
        form=QuoteForm(request.POST)
        if form.is_valid():
            print('valid')
    form = QuoteForm()
    return render(request,"quote/quote.html", {'form':form} )