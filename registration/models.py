from django.db import models
from django.core.validators import RegexValidator

class Register(models.Model):
    phone_validator = RegexValidator(r'^09\d{9}$', message= 'تلفن همراه را به درستی وارد کنید')
    fname = models.CharField(max_length= 25, verbose_name= 'نام')
    lname = models.CharField(max_length= 25, verbose_name= 'نام خانوادگی')
    num = models.CharField(
        max_length= 11,
        verbose_name= 'تلفن همراه',
        validators= [phone_validator]
    )
    user_name = models.CharField(max_length=23, verbose_name= 'نام کاربری')
    password = models.CharField(max_length=50, validators= [RegexValidator(
        regex= r'^[a-zA-Z0-9]{8,}$',
        message= 'رمز عبور باید حداقل 8 کاراکتر شامل حروف یا اعداد باشد'
    )])

    registered_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f'{self.fname}, {self.lname} - {self.registered_at}'
    