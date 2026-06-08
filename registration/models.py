from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from iranian_cities.fields import ProvinceField, CityField

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

    registered_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f'{self.fname}, {self.lname} - {self.registered_at}'
    
class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='info')
    degree_choices = [
        ('diploma', 'دیپلم'),
        ('associate', 'کاردانی'),
        ('bachelor', 'کارشناسی'),
        ('master', 'کارشناسی ارشد'),
        ('phd', 'دکتری')
    ]
    father_name = models.CharField(max_length=25, verbose_name='نام پدر', blank=True, null=True)
    national_num = models.CharField(
        max_length=10,
        verbose_name='کد ملی',
        validators=[RegexValidator(r'^\d{10}$', message='کد ملی باید شامل 10 رقم باشد')],
        blank=True, null=True
    )
    degree = models.CharField(max_length=25, choices=degree_choices, verbose_name='میزان تحصیلات', blank=True, null=True)
    national_card = models.FileField(upload_to='cards/', verbose_name='تصویر کارت ملی', blank=True, null=True)
    sex = models.CharField(max_length=10, choices=[('man', 'مرد'), ('woman', 'زن')], verbose_name='جنسیت', blank=True, null=True)
    birth_date = models.DateField(verbose_name='تاریخ تولد', blank=True, null=True)
    
    birth_province = ProvinceField(
        verbose_name='استان محل تولد', 
        blank=True,
        null=True,
        related_name='birth_info'
    )

    birth_city = CityField(
        verbose_name='شهر محل تولد',
        blank=True, 
        null=True,
        related_name='birth_info'
    )

    province = ProvinceField(
        verbose_name='استان محل سکونت', 
        blank=True, 
        null=True,
        related_name='residence_info'
    )

    city = CityField(
        verbose_name='شهر محل سکونت', 
        blank=True, 
        null=True,
        related_name='residence_info'
    )

    email = models.EmailField(verbose_name= 'ایمیل', blank= True, null= True)
    location = models.TextField(verbose_name='محل سکونت', blank=True, null=True)
    photo = models.FileField(verbose_name='عکس پرسنلی', blank=True, null=True)
    degree_certificate = models.FileField(verbose_name='تصویر مدرک تحصیلی', blank=True, null=True)