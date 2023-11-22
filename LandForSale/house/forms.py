# house/forms.py

from django import forms

class HouseSearchForm(forms.Form):
    location = forms.CharField(required=False)
    max_price = forms.DecimalField(required=False)
