from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class QuantityForm(forms.Form):
    qty = forms.IntegerField(min_value=1, initial=1)
    