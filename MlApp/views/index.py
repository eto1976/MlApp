from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):

    return render(request,'index.html')

def login(request):

    username = request.POST["username"]
    password = request.POST["password"]

    template = loader.get_template("top.html")
    context = {
        "username": username,
        "password": password,
    }

    return HttpResponse(template.render(context, request))
