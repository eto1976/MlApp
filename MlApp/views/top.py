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

    exOp = form.data['exOp']

    msg = "default"
    if exOp == "1" :

        # 画像学習処理
        msg = ImagelearnLogic.imageleanExec(form)

    elif exOp == "2" :

        # 画像判定処理
        msg = ImagelearnLogic.imageJudgmentExec(form)

    else :
        print("未処理")

    # From値のセット
    form.msg = msg

    template = loader.get_template("top.html")
    context = {
        "topForm": form,
    }

    return HttpResponse(template.render(context, request))
