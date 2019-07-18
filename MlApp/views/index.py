from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from MlApp.models.mstuser import Mst_user


def index(request):

    return render(request,'index.html')

def login(request):

    username = request.POST["username"]
    password = request.POST["password"]

    userInfo = []


#    for obj in Mst_user.objects.all():
#        userInfo.append(obj)

    template = loader.get_template("top.html")
    context = {
        "username": username,
        "password": password,
    }

    return HttpResponse(template.render(context, request))
