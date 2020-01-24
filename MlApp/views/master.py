from django.http.response import HttpResponse
from django.template import loader

from MlApp.forms.masterform import MasterForm
from MlApp.models.mstimagelabel import Mst_imagelabel
from MlApp.views.page import paginate_queryset


# 1ページの表示件数
pagecount = 5

# 処理実行またはリロード処理
def masterExecution(request):

    # 通常Form（※編集不可）
    masterForm = MasterForm(request.POST or None)
    # 編集用CopyForm
    masterFormcopy = MasterForm(request.POST.copy())

    msg=""

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

    # 登録ボタン押下時（画面遷移）
    elif 'doInsertDisp' in request.POST:

        template = loader.get_template("masterEdit.html")
        context = {
            "masterForm": masterForm,
        }

    # 修正ボタン押下時（画面遷移）
    elif 'doEditDisp' in request.POST:
        selectRadios = request.POST.get('selectRadios')
        imagelabel_ct = []
        for objimagelabel in Mst_imagelabel.objects.filter(labelclass=selectRadios):
            imagelabel_ct.append(objimagelabel)


        # 取得したフィールドの追加
        masterFormcopy.data['labelclass'] = imagelabel_ct[0].labelclass
        masterFormcopy.data['labelclassname'] = imagelabel_ct[0].labelclassname
        masterFormcopy.data['baselabelclass'] = imagelabel_ct[0].baselabelclass

        template = loader.get_template("masterEdit.html")
        context = {
            "masterForm": masterFormcopy,
        }

    # 登録処理
    elif 'doInsert' in request.POST:

        objimagelabel = Mst_imagelabel(
            labelclass=masterForm.data['labelclass'],
            labelclassname = masterForm.data['labelclassname'],
            baselabelclass = masterForm.data['baselabelclass'])

        objimagelabel.save()

        msg = "登録が行われました。"
        template = loader.get_template("masterEdit.html")
        context = {
            "masterForm": masterForm,
            "msg": msg,
        }

    # 修正処理
    elif 'doEdit' in request.POST:

        objimagelabel = Mst_imagelabel.objects.get(labelclass=masterForm.data['labelclass'])
        objimagelabel.labelclassname = masterForm.data['labelclassname']
        objimagelabel.baselabelclass = masterForm.data['baselabelclass']

        objimagelabel.save()

        msg = "修正が行われました。"
        template = loader.get_template("masterEdit.html")
        context = {
            "masterForm": masterForm,
            "msg": msg,
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
