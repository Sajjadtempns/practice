from django.shortcuts import render, redirect
from registration.forms import AdminLoginForm
from django.contrib.auth import authenticate, login
from captcha.models import CaptchaStore
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("/admin-panel/")

    form = AdminLoginForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            if user and user.is_staff:
                login(request, user)
                return redirect("/admin-panel/")

            form.add_error(None, "شما به پنل ادمین دسترسی ندارید")

    return render(request, "admin_login.html", {"form": form})

def captcha_refresh(request):
    new_key = CaptchaStore.generate_key()

    return JsonResponse({
        "key": new_key,
        "image_url": f"/captcha/image/{new_key}/"
    })