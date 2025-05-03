from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.
@login_required(login_url='/account/login')
def home(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'home.html', {'posts': posts})