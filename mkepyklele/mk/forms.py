
from django import forms
from django.core.validators import EmailValidator
from .models import NewsletterUser

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Jūsų vardas')
    email = forms.CharField(validators=[EmailValidator()], label='El. paštas')
    phone = forms.CharField(max_length=15, label='Telefono numeris')
    subject = forms.CharField(max_length=100, label='Tema')
    message = forms.CharField(widget=forms.Textarea, label='Jūsų žinutė')

class SubscribeNewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['user_email']
        labels = {
            'user_email': ''
        }

        def clean_email(self):
            email = self.cleaned_data.get('user_email')
            
            return email
