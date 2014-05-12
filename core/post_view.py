# -*- coding: utf-8-*-
from django.shortcuts import render
from core.models import Post
from django.http import HttpResponse
from core import crypt
import json

def render_to_json(dict):
    return HttpResponse(json.dumps(dict, sort_keys=True, indent=2),
        content_type='application/json; charset=UTF-8')


def home(request):
    return render(request, 'paste.html')

def add_post(request):
    params = request.POST
    text, login, name, password = (params['text'], params['login'], params['name'], params['password'])

    text = crypt.encrypt_text(password,text)
    passhash = crypt.hash_text(password)
    post = _get_post(login,name)
    if post:
        if passhash == post.password:
            post.text = text
            post.save()
            return render_to_json({'success': True})
        else:
         return render_to_json({'success': False})
    #create new post
    p = Post()
    p.text, p.login, p.name, p.password = text, login, name, passhash
    p.save()

    return render_to_json({'success': True})


def get_post(request):
    login = request.POST['login']
    name = request.POST['name']
    password = request.POST.get('password')
    passhash = crypt.hash_text(password)
    post = _get_post(login,name)
    if post and post.password == passhash:
        data = dict(name=name, login=login, text=crypt.decrypt_text(password,post.text))

        return render_to_json(dict(data=data,success=True))

    return render_to_json({'success': False})


def _get_post(login, name):
    posts = Post.objects.filter(login=login, name=name)
    if len(posts): return posts[0]
    return None


def open_post(request, login, name):
    post = _get_post(login, name)
    if not post:
        post = Post()
        post.login, post.name = login,name

    return render(request, 'paste.html', dict(post=post))


