from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def cadastro(request):

    if request.method == "GET":
        return render(request, 'cadastro.html')

    #print(request.POST.get('primeiro_nome'))
    #print(request.POST)
    #if request.method == "get":

    elif request.method == "POST":
        voltar1 = request.POST.get('voltar')
        if voltar1:
            return redirect('/usuarios/login')
        nome = request.POST.get('primeiro_nome')
        ultimo = request.POST.get('ultimo_nome')
        usuario = request.POST.get('username')
        senha1 = request.POST.get('senha')
        email1 = request.POST.get('email')
        confirma = request.POST.get('confirmar_senha')

        if nome == "" or ultimo =="" or usuario =="" or senha1 =="" or email1 =="" or confirma =="":
            messages.add_message(request, constants.INFO, 'EXISTE ESPAÇO EM BRANCO NOS CAMPOS ')
            return redirect('/usuarios/cadastro')



        if not senha1 == confirma:
            messages.add_message(request,constants.ERROR,'As senhas não são iguais ')
            return redirect('/usuarios/cadastro')
        #elif len(senha1) < 6:
            #messages.add_message(request, constants.INFO, 'SUA SENHA DEVE CONTER MAIS DE 6 CARACTERES')
            #return redirect('/usuarios/cadastro')
        #elif senha1 == confirma:
            #return HttpResponse("boa FILHA DA PUTA ")

        user = User.objects.create_user(
            first_name = nome,
            last_name = ultimo,
            username=usuario,
            password=senha1,
            email=email1

        )

        messages.add_message(request, constants.SUCCESS, 'USUARIO CADASTRADO COM SUCESSO')
        return redirect('/usuarios/cadastro')


def logar(request):
    if request.method == "GET":
        return render(request,'login.html')

    elif request.method == "POST":
        cadastro = request.POST.get('ultimo_nome')
        if cadastro:
            return redirect('/usuarios/cadastro')
    #else:

        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user:
            login(request, user)
    # Acontecerá um erro ao redirecionar por enquanto, resolveremos nos próximos passos
            return redirect('/exames/solicitar_exames/')
            #return HttpResponse("logado")

        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
            return redirect('/usuarios/login')










