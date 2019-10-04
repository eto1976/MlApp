from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from MlApp.batch.imagelearnLogic import ImagelearnLogic
from MlApp.forms.topform import TopForm


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

    if exOp == "1" :

        # 画像学習処理
        msg = ImagelearnLogic.imageleanExec(form)

    elif exOp == "2" :

        # 画像判定処理
        msg = ImagelearnLogic.imageJudgmentExec(form)

    else :
        msg = "実行に失敗しました。"

    # From値のセット

    template = loader.get_template("top.html")
    context = {
        "dataFolder": dataFolder,
        "testFile": testFile,
        "msg": msg,
    }

    return HttpResponse(template.render(context, request))
