from django import forms
from .models import Profile
from django.core.validators import RegexValidator


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100,
                               validators= [RegexValidator(
                                   regex= r'^[a-zA-Z0-9]{8,}$',
                                   message= 'رمز عبور باید حداقل 8 کاراکتر شامل حروف یا اعداد باشد')],
                                   widget= forms.PasswordInput(attrs= {'class': 'form-control input-lg text-end',
                                                                       'placeholder': 'حداقل 8 کاراکتر؛ شامل حروف و اعداد'
                                                                       }
                                                                ),
                                                                label= 'رمز ورود'
    )

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-end'}), label='نام کاربری')
    
    class Meta:
        model = Profile
        fields = ["fname", "lname", "num", "username", "password"]
        widgets = {
            "fname": forms.TextInput(attrs= {'class': 'form-control text-end'}),
            "lname": forms.TextInput(attrs= {'class': 'form-control text-end'}),
            "num": forms.TextInput(attrs= {'class': 'form-control text-end', 'placeholder': '09123456789'}),
            #"username": forms.TextInput(attrs= {'class': 'form-control text-end'}),
            #"password": forms.PasswordInput(attrs= {'class': 'form-control text-end'})
        }
