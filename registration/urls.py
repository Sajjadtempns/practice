from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name= 'register'),
    path('profile/', views.profile, name= 'profile'),
    path('loging_out', view= views.loging_out, name= 'loging_out')
]