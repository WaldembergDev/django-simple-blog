from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Categories, Post
from django.utils import timezone

# Create your views here.
@login_required(login_url='/account/login/')
def new_post(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        return render(request, 'new_post.html', {'categories': categories})
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user
        created_in = timezone.now()
        categorie = request.POST.get('categorie')
        model_categorie = Categories.objects.filter(name = categorie).first()
        new_post = Post(
            title = title,
            content = content,
            author = author,
            created_in = created_in,
            categories = model_categorie
        )
        new_post.save()
        return redirect('/posts/new_post')

@login_required(login_url='/account/login/')
def delete_post(request, id):
    post = Post.objects.filter(id = id).first()
    post.delete()
    return redirect('/plataform/home/')

def edit_post(request, id):
    pass
