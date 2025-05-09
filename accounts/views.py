from django.shortcuts import render, redirect
from .models import CustomUser, GenderEnum
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def login(request):
    # verificando se o usuário está autenticado
    if request.user.is_authenticated:
        return redirect('/plataform/home')
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email:
            messages.add_message(request, constants.WARNING, 'É necessário informar um e-mail!')
            return redirect('/account/login/')
        if not password:
            messages.add_message(request, constants.WARNING, 'É necessário informar uma senha!')
            return redirect('/account/login/')
        user = auth.authenticate(request, email=email, password=password)
        if user:
            auth.login(request, user)
            return redirect('/account/login/')
        messages.add_message(request, constants.WARNING, 'Login ou senha inválidos!')
        return redirect('/account/login/')

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
            messages.add_message(request, constants.WARNING, 'Já existe um cadastro com esse e-mail!')
            return redirect('/account/register/')
        if not first_name:
            messages.add_message(request, constants.WARNING, 'É obrigatório informar o primeiro nome!')
            return redirect('/account/register/')
        if not surname:
            messages.add_message(request, constants.WARNING, 'É obrigatório informar o sobrenome!')
            return redirect('/account/register/')
        if not email:
            messages.add_message(request, constants.WARNING, 'É obrigatório informar o e-mail!')
            return redirect('/account/register/')
        if not password:
            messages.add_message(request, constants.WARNING, 'É obrigatório fornecer uma senha!')
            return redirect('/account/register/')
        if not date_of_birth:
            messages.add_message(request, constants.WARNING, 'É obrigatório fornecessar uma data de nascimento!')
            return redirect('/account/register/')
        if not gender:
            messages.add_message(request, constants.WARNING, 'É obrigatório informar o gênero!')
            return redirect('/account/register/')
        user = CustomUser.objects.create_user(
            first_name = first_name,
            surname = surname,
            email = email,
            password = password,
            date_of_birth = date_of_birth,
            gender = gender
        )
        user.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect('/plataform/home')

def logout(request):
   auth.logout(request)
   return redirect('/account/login')

@login_required(login_url='/account/login')
def my_account(request):
    if request.method == 'GET':
        # salvando os gêneros em uma lista
        genders = [gender.value for gender in GenderEnum]
        return render(request, 'my_account.html', {'genders': genders})
    else:
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # obtendo o usuário logado
        user = request.user
        # validando os campos
        if not first_name:
            messages.add_message(request, constants.WARNING, 'O nome do usuário não pode estar vazio!')
            return redirect('/account/my_account/')
        if not surname:
            messages.add_message(request, constants.WARNING, 'O sobrenome não pode estar vazio!')
            return redirect('/account/my_account/')
        if not email:
            messages.add_message(request, constants.WARNING, 'O e-mail não pode estar vazio!')
            return redirect('/account/my_account/')
        if not date_of_birth:
            messages.add_message(request, constants.WARNING, 'A data de nascimento não pode estar vazia!')
            return redirect('/account/my_account/')
        if password != confirm_password:
            messages.add_message(request, constants.WARNING, 'As senhas digitadas não são iguais não pode estar vazia!')
            return redirect('/account/my_account/')
        # atualizando os dados do usuário
        user.first_name = first_name
        user.surname = surname
        user.email = email
        user.date_of_birth = date_of_birth
        user.gender = gender
        # atualizando a senha se ela tiver sido preenchida
        if password:
            user.set_password(password)
        # atualizando no banco de dados
        user.save()
        # permanecendo o usuário logado caso ele tenha alterado a senha
        update_session_auth_hash(request, user)
        # mostrando uma mensagem de confirmação ao usuário
        messages.add_message(request, constants.SUCCESS, 'Dados alterados com sucesso!')
        # redirecionando o usuário para a mesma url
        return redirect('/account/my_account')