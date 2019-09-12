from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from MlApp.forms.topform import TopForm


def top(request):
    return render(request,'top.html')

def work(request):
    return render(request,'work.html')

def execution(request):

    form = TopForm(request.POST or None)

    data = form.data['data']
    testFile = form.data['testFile']
    exOp = form.data['exOp']

    msg = "default"
    if exOp == "1" :



        msg = "訓練結果"

    else :
        msg = "テスト結果"


    template = loader.get_template("top.html")
    context = {
        "data": data,
        "testFile": testFile,
        "msg": msg,
    }

    return HttpResponse(template.render(context, request))
