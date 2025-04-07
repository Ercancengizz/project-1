# forms.py
from django import forms
from auths.models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username', 'email', 'password'] 

    password = forms.CharField(widget=forms.PasswordInput) 
