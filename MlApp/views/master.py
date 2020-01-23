from django.http.response import HttpResponse
from django.template import loader

from MlApp.models.mstimagelabel import Mst_imagelabel


# 処理実行またはリロード処理
def masterExecution(request):

    # 検索ボタン押下時
    if 'doSearch' in request.POST:
        # 検索処理
        imagelabelList = Mst_imagelabel.objects.all()

        template = loader.get_template("master.html")
        context = {
            "imagelabelList": imagelabelList,
        }

    # 登録ボタン押下時
    elif 'doInsert' in request.POST:
        imagelabelList = Mst_imagelabel.objects.all()

        template = loader.get_template("masterEdit.html")
        context = {
        }

    # 修正ボタン押下時
    elif 'doEdit' in request.POST:
        imagelabelList = Mst_imagelabel.objects.all()

        template = loader.get_template("masterEdit.html")
        context = {
        }

    # 削除ボタン押下時
    elif 'doDelete' in request.POST:
        imagelabelList = Mst_imagelabel.objects.all()

        template = loader.get_template("master.html")
        context = {
            "imagelabelList": imagelabelList,
        }


    return HttpResponse(template.render(context, request))
