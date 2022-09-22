from django import forms


class ContactForm(forms.Form):
    firstname = forms.CharField(required=True, max_length=255)
    lastname = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
