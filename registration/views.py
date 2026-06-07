from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Profile, Info
from .forms import UserRegistrationForm, ProfileEditInfo
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from iranian_cities.models import City

def register(request):
    if request.user.is_authenticated:
        return redirect(to= 'profile')
    elif request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
                email = form.cleaned_data['email'],
                first_name = form.cleaned_data['fname'],
                last_name = form.cleaned_data['lname']
            )
            profile = form.save(commit= False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    context = {
        'user': user,
        'profile': user.profile
    }
    return render(request, 'registration/profile.html', context=context)

def loging_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect(to= 'login')
    return render(request, 'registration/loging_out.html')

@login_required
def edit(request):
    profile = Profile.objects.get(user=request.user)
    info, created = Info.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        info_form = ProfileEditInfo(request.POST, request.FILES, instance=info)
        if info_form.is_valid():
            info_form.save()
            profile.fname = info_form.cleaned_data.get('fname', profile.fname)
            profile.lname = info_form.cleaned_data.get('lname', profile.lname)
            profile.save()

            user = request.user
            user.email = info_form.cleaned_data.get('email', user.email)
            user.first_name = info_form.cleaned_data.get('fname', user.first_name)
            user.last_name = info_form.cleaned_data.get('lname', user.last_name)
            user.save()
            
            return redirect('profile')
    else:
        info_form = ProfileEditInfo(instance=info)
        info_form.fields['fname'].initial = profile.fname
        info_form.fields['lname'].initial = profile.lname
        info_form.fields['email'].initial = request.user.email
    
    return render(request, 'registration/edit.html', {'form': info_form})

def load_cities(request):
    province_id = request.GET.get('province_id')
    if province_id:
        cities = City.objects.filter(province_id=province_id).values('id', 'name')
        return JsonResponse(list(cities), safe=False)
    return JsonResponse([], safe=False)