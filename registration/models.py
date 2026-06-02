from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, verbose_name= 'کاربر')
    phone_validator = RegexValidator(r'^09\d{9}$', message= 'مثال: 09123456789')
    fname = models.CharField(max_length= 25, verbose_name= 'نام')
    lname = models.CharField(max_length= 25, verbose_name= 'نام خانوادگی')
    num = models.CharField(
        max_length= 11,
        verbose_name= 'تلفن همراه',
        validators= [phone_validator]
    )
    # username = models.CharField(max_length=23, verbose_name= 'نام کاربری')
    # password = models.CharField(max_length=50, validators= [RegexValidator(
    #    regex= r'^[a-zA-Z0-9]{8,}$',
    #    message= 'رمز عبور باید حداقل 8 کاراکتر شامل حروف یا اعداد باشد'
    #)])

    registered_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f'{self.fname}, {self.lname} - {self.registered_at}'
    