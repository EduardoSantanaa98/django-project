from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já existe.")
            return redirect('registro')

        user = User.objects.create_user(username=username, 
                                        email=email, 
                                        password=password)
        user.save()
        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('login')

    
    return render(request, 'usuarios/registro.html')

def fazer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            request.session['nome_completo'] = user.username
            request.session['email'] = user.email
            request.session['tema_preferido'] = 'escuro'
            
            messages.success(request, "Login realizado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Credenciais inválidas.")
            return redirect('login')

    return render(request, 'usuarios/login.html')

def fazer_logout(request):
    logout(request)
    request.session.flush()
    messages.success(request,"Você saiu da conta.")
    return redirect('login')

@login_required
def home(request):
    nome_completo = request.session.get('nome_completo', 'Usuário')
    email = request.session.get('email', 'sem email')
    tema = request.session.get('tema_preferido', 'padrão')

    contexto = {
        'nome_completo': nome_completo,
        'email': email,
        'tema': tema,
    }
    
    return render(request, 'usuarios/home.html', contexto)

# Create your views here.