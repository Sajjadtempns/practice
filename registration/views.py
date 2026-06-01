from django.shortcuts import render

def register(request):
    #if request.method == 'POST':
    return render(request, 'registration/register.html')
