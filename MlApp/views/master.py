from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from MlApp.models.mstimagelabel import Mst_imagelabel
from MlApp.forms.toolsform import ToolsForm


# 実行またはリロード処理
def masterExecution(request):

    # 実行ボタン押下時
    if 'doSearch' in request.POST:
        # 検索処理
        imagelabelList = Mst_imagelabel.objects.all()
        #ディクショナリーの形で設定

    template = loader.get_template("master.html")
    context = {
        "imagelabelList": imagelabelList,
    }

    return HttpResponse(template.render(context, request))
