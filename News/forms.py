from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 50, required = True)
    email = forms.EmailField(max_length = 50, required = True)
    content = forms.CharField(max_length = 255, widget = forms.Textarea(), required = True)