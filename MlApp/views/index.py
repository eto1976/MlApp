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

# 初期表示
def index(request):

    return render(request,'index.html')

# ログイン処理
def login(request):

    #フォーム取得と初期化
    form = IndexForm(request.POST or None)
    topform = TopForm()

    username = form.data['username']
    password = form.data['password']

    userInfo = []
    msg = ""

    # ユーザ情報取得
    for objuser in Mst_user.objects.filter(id = username):
        userInfo.append(objuser)

    # ユーザ認証 ※デバック時はスキップ
    if debugMode != True:

        if len(userInfo) > 0 and userInfo[0].password == password :
            template = loader.get_template("top.html")
        else :
            template = loader.get_template("index.html")
            msg = "ユーザIDまたはパスワードが不正です。"

            context = {
                "msg": msg,
            }
            return HttpResponse(template.render(context, request))

    else :
            template = loader.get_template("top.html")

    #セッションにユーザ情報保持
    request.session['username'] = username
    request.session['password'] = password

    #プルダウン初期値追加のカテゴリー1のみ追加
    #カテゴリー1
    imagelabel_ct1 = []
    CATEGORIES_1 = ()

    for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass__isnull=True):
        imagelabel_ct1.append(objimagelabel)

    for imagelabel_ct1_obj in imagelabel_ct1:
        CATEGORIES_1_GET = (
            (imagelabel_ct1_obj.labelclass, imagelabel_ct1_obj.labelclassname),
        )

        CATEGORIES_1 = CATEGORIES_1 + CATEGORIES_1_GET

    #選択肢追加
    EMPTY_CHOICES_1 = (
        ('', '-----ラベル階層1-----'),
    )

    topform.fields['category_1'].choices = EMPTY_CHOICES_1 + CATEGORIES_1

    context = {
        "username": username,
        "password": password,
        "msg": msg,
        "topForm": topform,
    }

    return HttpResponse(template.render(context, request))
