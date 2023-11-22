# land/forms.py

from django import forms

class LandSearchForm(forms.Form):
    location = forms.CharField(required=False)
    max_price = forms.DecimalField(required=False)
