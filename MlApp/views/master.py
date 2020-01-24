from django.http.response import HttpResponse
from django.template import loader

from MlApp.models.mstimagelabel import Mst_imagelabel
from MlApp.views.page import paginate_queryset

# 1ページの表示件数
pagecount = 10

# 処理実行またはリロード処理
def masterExecution(request):

    # 検索ボタン押下時
    if 'doSearch' in request.POST:
        # 検索処理
        imagelabelList = Mst_imagelabel.objects.all()
        #ページング処理（第3引数が1ページの表示件数）
        page_obj = paginate_queryset(request, imagelabelList, pagecount)

        template = loader.get_template("master.html")
        context = {
            "imagelabelList": page_obj.object_list,
            'page_obj': page_obj,
        }

    # クリアボタン押下時
    elif 'doClear' in request.POST:
        # 検索処理
        imagelabelList = []

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

    # ページング処理（ここだけgetのみ）
    elif request.GET.get('page'):
        # 検索処理
        imagelabelList = Mst_imagelabel.objects.all()
        #ページング処理
        page_obj = paginate_queryset(request, imagelabelList, pagecount)

        template = loader.get_template("master.html")
        context = {
            "imagelabelList": page_obj.object_list,
            'page_obj': page_obj,
        }

    return HttpResponse(template.render(context, request))
