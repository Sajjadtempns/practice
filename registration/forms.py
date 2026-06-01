from django import forms
from .models import Register

class User(forms.ModelForm):
    class Meta:
        model = Register,
        fields = ["fname", "lname", "num", "user_name", "password"]
        widgets = {
            "fname": forms.TextInput(attrs= {'class': 'form-control'}),
            "lname": forms.TextInput(attrs= {'class': 'form-control'}),
            "num": forms.TextInput(attrs= {'class': 'form-control'}),
            "user_name": forms.TextInput(attrs= {'class': 'form-control'}),
            "password": forms.PasswordInput(attrs= {'class': 'form-control'})
        }
