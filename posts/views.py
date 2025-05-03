from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Categories, Post
from django.utils import timezone
from django.contrib import messages
from django.contrib.messages import constants

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
    # criando uma mensagem
    messages.add_message(request, constants.SUCCESS, 'Post deletado com sucesso!')
    return redirect('/plataform/home/')

def edit_post(request, id):
    post = Post.objects.filter(id = id).first()
    categories = Categories.objects.all()
    if request.method == 'GET':
        return render(request, 'edit_post.html', {'post': post, 'categories': categories})
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        categorie = request.POST.get('categorie')
        update_in = timezone.now()
        # obtendo a categoria
        model_categorie = Categories.objects.filter(name = categorie).first()
        # atualizando o post
        post.title = title
        post.content = content
        post.categories = model_categorie
        post.updated_in = update_in
        # salvando as alterações do post
        post.save()
        # criando uma mensagem
        messages.add_message(request, constants.SUCCESS, 'Post atualizado com sucesso!')
        # redirecionando o usuário para a mesma página
        return redirect('edit_post', id=post.id)
                
    
