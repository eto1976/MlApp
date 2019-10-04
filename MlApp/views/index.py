from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from MlApp.forms.indexform import IndexForm
from MlApp.forms.topform import TopForm
from MlApp.models.mstimagelabel import Mst_imagelabel
from MlApp.models.mstuser import Mst_user

# デバックモード取得
debugMode = getattr(settings, "DEBUG", None)

def index(request):

    return render(request,'index.html')

def login(request):

    form = IndexForm(request.POST or None)
    topform = TopForm()

    username = form.data['username']
    password = form.data['password']

    userInfo = []
    imagelabel = []
    msg = ""

    # ユーザ情報取得
    for objuser in Mst_user.objects.filter(id = username):
        userInfo.append(objuser)

    # ラベルプルダウンリスト取得
    for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass__isnull=True):
        imagelabel.append(objimagelabel)

    # ユーザ認証 ※デバック時はスキップ
    if debugMode != True:

        if len(userInfo) > 0 and userInfo[0].password == password :
            template = loader.get_template("top.html")
        else :
            template = loader.get_template("index.html")
            msg = "ユーザIDまたはパスワードが不正です。"
    else :
            template = loader.get_template("top.html")

    context = {
        "username": username,
        "password": password,
        "msg": msg,
        "topForm": topform,
    }

    return HttpResponse(template.render(context, request))
