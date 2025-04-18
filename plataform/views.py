from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/account/login')
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')