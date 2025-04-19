from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/account/login/')
def new_post(request):
    return render(request, 'new_post.html')


        
