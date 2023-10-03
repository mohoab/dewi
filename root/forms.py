from django import forms
from .models import Newsletter , Contact_f
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']

class ContectForm(forms.ModelForm):
    class Meta:
        model = Contact_f
        fields = [
            'subject',
            'name',
            'email',
            'message',
        ]
