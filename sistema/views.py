# -*- coding: utf-8 -*-

from django.shortcuts import render
# from django import simplejson as json
import json
from forms import *
from models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.
def login(request):
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid:
            username = request.POST.get('email')
            password = request.POST.get('password')
            print username
            print password
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/home/')
        else:
            print loginForm
            mostra_mensagem = True
    return render(request, 'login.html', locals())


@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')


def home(request):
    user = request.user

    lista_posts = Post.objects.all()
    lista_final = []

    for post in lista_posts:
        status = False
        try:
            status = Status_curtida.objects.get(user=user, post=post).curtiu
        except Exception, e:
            status = False

        texto_cortado = post.conteudo[0:600]
        texto_cortado = texto_cortado.rsplit('.',1)[0]+'.'

        post_cortado = [post.titulo, texto_cortado, post.id]
        lista_final.append([post_cortado,status])
    return render(request, 'home.html', locals())


@login_required
def curtir_post(request):
    user = request.user

    post_id = request.POST.get("post_id", False)
    post = Post.objects.get(id=post_id)

    try:
        curtida = Status_curtida.objects.get(user=user, post=post)
        curtida.curtiu = not(curtida.curtiu)
        curtida.save()
        status = curtida.curtiu
    except Exception, e:
        print "Erro: " + str(e)
        curtida = Status_curtida(user = user, post = post, curtiu = True)
        curtida.save()
        status = True

    if status:
        resposta = "Curtiu"
    else:
        resposta = "Descurtiu"

    return HttpResponse(resposta)


def ver_post(request, post_id):
    user = request.user

    post = Post.objects.get(id=post_id)
    lista_paragrafos = post.conteudo.split('\n', 1)
    lista_paragrafos[1] = lista_paragrafos[1].split('\n')

    comentarios = Comentario.objects.filter(post=post)
    lista_comentarios = []
    for comm in comentarios:
        lista_comentarios.append([comm, comm.autor==user])

    print lista_comentarios

    return render(request, "ver_post.html", locals())

@login_required
def comentar_post(request):
    print '-------------'
    resposta = {}
    if request.method == 'POST':
        try:
            print request.POST
            comentario = request.POST.get('comentario')
            print comentario
            post_id = request.POST.get('post_id')
            print post_id

            post = Post.objects.get(id=post_id)
            comentario = Comentario(post=post, autor=request.user, texto=comentario)
            comentario.save()

            resposta['status'] = "OK"

        except Exception, e:
            print e
            resposta['status'] = "BAD"

        return HttpResponse(json.dumps(resposta), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"Nada aqui para ver":"nao adianta tentar"}), content_type="application/json")


def cadastrar(request):
    cadastroForm = CadastroForm()
    if request.method == 'POST':
        cadastroForm = CadastroForm(request.POST)
        if cadastroForm.is_valid():
            cadastroForm = cadastroForm.cleaned_data
            user = User.objects.create_user(
                cadastroForm['email'],
                email = cadastroForm['email'],
                password = cadastroForm['password'],
                first_name = cadastroForm['first_name'],
                last_name = cadastroForm['last_name'],
                )
            print '**********'
            user_auth = authenticate(username=cadastroForm['email'], password=cadastroForm['password'])
            # user_auth = authenticate(username='marcos', password='marcos')
            print user_auth
            auth_login(request, user_auth)
            return HttpResponseRedirect('/home/')
        else:
            erro = True
            # return HttpResponse('<script>history.back(); $(function() {$("#error_message").show()});</script>')

    return render(request, 'cadastrar.html', locals())


@login_required
def apagar_comentario(request, comm_id):
    try:
        comentario = Comentario.objects.get(id=comm_id)
        if comentario.autor == request.user:
            comentario.delete()

        return HttpResponseRedirect('/ver_post/'+str(comentario.post.id))
    except:
        return HttpResponse('<script>history.back()</script>')

