from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from MlApp.batch.imagelearnLogic import ImagelearnLogic
from MlApp.forms.topform import TopForm
from MlApp.models.mstimagelabel import Mst_imagelabel


def top(request):
    return render(request,'top.html')

def work(request):
    return render(request,'work.html')

def execution(request):

    form = TopForm(request.POST or None)

    dataFolder = form.data['dataFolder']
    testFile = form.data['testFile']
    exOp = form.data['exOp']
    msg = form.data['msg']

    # 実行ボタン押下時
    if 'doExecute' in request.POST:

        if exOp == "1" :

            # 画像学習処理
            msg = ImagelearnLogic.imageleanExec(form)

        elif exOp == "2" :

            # 画像判定処理
            msg = ImagelearnLogic.imageJudgmentExec(form)

        else :
            msg = "実行に失敗しました。"
    else :
        #選択肢動的変更
        #イメージラベルオブジェクト
        imagelabel_ct1 = []
        imagelabel_ct2 = []
        imagelabel_ct3 = []

        EMPTY_CHOICES_2 = (
            ('', '-----ラベル階層2-----'),
        )
        EMPTY_CHOICES_3 = (
            ('', '-----ラベル階層3-----'),
        )

        #カテゴリー2
        CATEGORIES_2 = ()

        for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass=form.data['category_1']):
            imagelabel_ct2.append(objimagelabel)

        for imagelabel_ct2_obj in imagelabel_ct2:
            CATEGORIES_2_GET = (
                (imagelabel_ct2_obj.labelclass, imagelabel_ct2_obj.labelclassname),
            )

            CATEGORIES_2 = CATEGORIES_2 + CATEGORIES_2_GET

        #カテゴリー3
        CATEGORIES_3 = ()

        for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass=form.data['category_2']):
            imagelabel_ct3.append(objimagelabel)

        for imagelabel_ct3_obj in imagelabel_ct3:
            CATEGORIES_3_GET = (
                (imagelabel_ct3_obj.labelclass, imagelabel_ct3_obj.labelclassname),
            )

            CATEGORIES_3 = CATEGORIES_3 + CATEGORIES_3_GET

        #取得したフィールドの追加
        form.fields['category_2'].choices = EMPTY_CHOICES_2 + CATEGORIES_2
        form.fields['category_3'].choices = EMPTY_CHOICES_3 + CATEGORIES_3



    template = loader.get_template("top.html")
    context = {
        "dataFolder": dataFolder,
        "testFile": testFile,
        "msg": msg,
        "topForm": form,
    }

    return HttpResponse(template.render(context, request))
