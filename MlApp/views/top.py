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
    radio = request.POST["exOp"]

    msg = "結果メッセージ"

    template = loader.get_template("top.html")
    context = {
        "msg": msg,
    }

    return HttpResponse(template.render(context, request))
