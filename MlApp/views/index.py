import logging

from django.conf import settings
from django.http.response import HttpResponse
from django.template import loader

from MlApp.forms.indexform import IndexForm
from MlApp.forms.topform import TopForm
from MlApp.models.mstimagelabel import Mst_imagelabel
from MlApp.models.mstuser import Mst_user


# デバックモード取得
debugMode = getattr(settings, "DEBUG", None)

# ログ変数
logger = logging.getLogger('command')

# 初期表示
def index(request):

    # 通常Form（※編集不可）
    form = IndexForm(request.POST or None)

    template = loader.get_template("index.html")

    if debugMode == True:
        msg = "デバックモード(ログイン認証なし)"

    context = {
        "indexForm": form,
        "msg": msg,
    }

    request.session.clear()

    return HttpResponse(template.render(context, request))

# ログイン処理
def login(request):

    # 通常Form（※編集不可）
    form = IndexForm(request.POST or None)

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
            logger.info("ログインユーザ ... [%s]" % userInfo[0].username)

        else :
            template = loader.get_template("index.html")
            msg = "ユーザIDまたはパスワードが不正です。"

            context = {
                "indexForm": form,
                "msg": msg,
            }
            return HttpResponse(template.render(context, request))

    else :
            template = loader.get_template("top.html")

    # セッションにユーザ情報保持
    request.session['username'] = username
    request.session['password'] = password

    # プルダウン初期値追加のカテゴリー1のみ追加
    # カテゴリー1
    imagelabel_ct1 = []
    CATEGORIES_1 = ()

    for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass__isnull=True):
        imagelabel_ct1.append(objimagelabel)

    for imagelabel_ct1_obj in imagelabel_ct1:
        CATEGORIES_1_GET = (
            (imagelabel_ct1_obj.labelclass, imagelabel_ct1_obj.labelclassname),
        )

        CATEGORIES_1 = CATEGORIES_1 + CATEGORIES_1_GET

    # 選択肢追加
    EMPTY_CHOICES_1 = (
        ('', '-----ラベル階層1-----'),
    )

    # Top画面初期値設定
    topform = TopForm()
    topform.fields['category_1'].choices = EMPTY_CHOICES_1 + CATEGORIES_1

    context = {
        "topForm": topform,
    }

    return HttpResponse(template.render(context, request))
