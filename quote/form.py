from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        models=Quote
        fields=[
            "first_name",
            "last_name",
            "email",
            "phone",
            "message",
        ]