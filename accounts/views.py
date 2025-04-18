from django.shortcuts import render, redirect
from .models import CustomUser

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        user_exist = CustomUser.objects.filter(email = email).exists()
        if user_exist:
            return redirect('/account/register/?status=error_1')
        user = CustomUser.objects.create_user(
            first_name = first_name,
            surname = surname,
            email = email,
            password = password,
            date_of_birth = date_of_birth,
            gender = gender
        )
        user.save()
        return redirect('/account/register/')
