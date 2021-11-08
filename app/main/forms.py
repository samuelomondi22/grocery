from django import forms
from .models import groceries

class StockForm(forms.ModelForm):
    class Meta:
        model = groceries
        fields = [
            'item',
            'walmart_price',
            'broulims_price',
            'albertsons_price'
        ]