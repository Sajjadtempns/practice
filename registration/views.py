from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect(to= 'profile')
    elif request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username= form.cleaned_data['username'],
                password= form.cleaned_data['password']
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

