from django import forms
from .models import groceries

class StockForm(forms.ModelForm):
    class Meta:
        model = groceries
        fields = [
            'ticker',
            'ask',
            'bid',
            'owned'
        ]