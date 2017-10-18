from django import forms
from .models import Registration, Loging



class RegisForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'phone', 'email']

class LogForm(forms.ModelForm):
    class Meta:
        model = Loging
        fields = ['user_email', 'user_password']