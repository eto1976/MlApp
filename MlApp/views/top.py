from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

def top(request):
    return render(request,'top.html')

def work(request):
    return render(request,'work.html')

def execution(request):
    data = request.POST["data"]
    testFile = request.POST["testFile"]
    exOp = request.POST["exOp"]

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
