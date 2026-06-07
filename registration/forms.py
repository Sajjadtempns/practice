from django import forms
from .models import Profile, Info
from django.core.validators import RegexValidator
from iranian_cities.models import City


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-end'}), label='نام کاربری')

    password = forms.CharField(validators= [RegexValidator(
                                regex= r'^[a-zA-Z0-9]{8,}$',
                                message= 'رمز عبور باید حداقل 8 کاراکتر شامل حروف یا اعداد باشد')],
                                widget= forms.PasswordInput(attrs= {'class': 'form-control input-lg text-end',
                                                                    'placeholder': 'حداقل 8 کاراکتر؛ شامل حروف و اعداد'
                                                                    }
                                                            ),
                                                            label= 'رمز ورود'
    )

    email = forms.EmailField(widget= forms.EmailInput(attrs= {'class': 'form-control'}), label= 'ایمیل')
    
    class Meta:
        model = Profile
        fields = ["fname", "lname", "num", "email", "username", "password"]
        widgets = {
            "fname": forms.TextInput(attrs= {'class': 'form-control text-end'}),
            "lname": forms.TextInput(attrs= {'class': 'form-control text-end'}),
            "num": forms.TextInput(attrs= {'class': 'form-control text-end', 'placeholder': '09123456789'}),
        }
  
class ProfileEditInfo(forms.ModelForm):

    fname = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control text-end'}),
        label='نام',
        required=False
    )
    lname = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control text-end'}),
        label='نام خانوادگی',
        required=False
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control text-end'}),
        label='ایمیل',
        required=False
    )

    birth_date = forms.DateField(
        widget= forms.DateInput(attrs= {'class': 'form-control text-end', 'type': 'date'}),
        label= 'تاریخ تولد',
        required=False
    )

    photo= forms.ImageField(
        widget= forms.FileInput(attrs= {'class': 'form-control'}),
        label= 'عکس پرسنلی',
        required=False
    )

    degree_certificate = forms.FileField(
        widget= forms.FileInput(attrs= {'class': 'form-control'}),
        label= 'مدرک تحصیلی',
        required=False
    )

    national_card = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='تصویر کارت ملی',
        required=False
    )


    class Meta:
        model = Info
        fields = ['father_name', 'degree', 'national_num', 'national_card', 'sex', 'birth_date', 'birth_province',
                  'birth_city', 'province', 'city', 'location', 'photo', 'degree_certificate']
        
        labels = {
            'father_name': 'نام پدر',
            'sex': 'جنسیت',
            'national_num': 'کد ملی',
            'birth_province': 'استان محل تولد',
            'birth_city': 'شهر محل تولد',
            'province': 'استان محل سکونت',
            'city': 'شهر محل سکونت',
            'location': 'آدرس محل سکونت',
            'degree': 'تحصیلات'
        }

        widgets = {
            "father_name": forms.TextInput(attrs= {'class': 'form-control text-end'}),
            "sex": forms.Select(attrs= {'class': 'form-control text-end'}),
            "national_num": forms.TextInput(attrs= {'class': 'form-control text-end'}),
            "birth_province": forms.Select(attrs= {'class': 'form-control text-end'}),
            "birth_city": forms.Select(attrs= {'class': 'form-control text-end'}),
            "province": forms.Select(attrs= {'class': 'form-control text-end'}),
            "city": forms.Select(attrs= {'class': 'form-control text-end'}),
            "location": forms.Textarea(attrs= {'class': 'form-control text-end'}),
            "degree": forms.Select(attrs= {'class': 'form-control text-end', 'placeholder': 'انتخاب کنید'}),
        }
        
        def __init__(self, *args, **kwargs):
            super.__init__(*args, **kwargs)
            self.fields["birth_city"].queryset = City.objects.none()
            self.fields["city"].queryset = City.objects.none()

            if self.instance and self.instance.pk:
                if self.instance.birth_province:
                    self.fields["birth_province"].queryset = City.objects.filter(province = self.instance.birth_province)
                if self.instance.province:
                    self.fields['city'].queryset = City.objects.filter(province=self.instance.province)
