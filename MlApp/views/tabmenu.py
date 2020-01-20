from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from MlApp.forms.topform import TopForm
from MlApp.models.mstimagelabel import Mst_imagelabel


# タブ（Top）処理
def disptop(request):

    topform = TopForm()
    #プルダウン初期値追加のカテゴリー1のみ追加
    #カテゴリー1
    imagelabel_ct1 = []
    CATEGORIES_1 = ()

    for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass__isnull=True):
        imagelabel_ct1.append(objimagelabel)

    for imagelabel_ct1_obj in imagelabel_ct1:
        CATEGORIES_1_GET = (
            (imagelabel_ct1_obj.labelclass, imagelabel_ct1_obj.labelclassname),
        )

        CATEGORIES_1 = CATEGORIES_1 + CATEGORIES_1_GET

    #選択肢追加
    EMPTY_CHOICES_1 = (
        ('', '-----ラベル階層1-----'),
    )

    topform.fields['category_1'].choices = EMPTY_CHOICES_1 + CATEGORIES_1

    template = loader.get_template("top.html")
    context = {
        "topForm": topform,
    }

    return HttpResponse(template.render(context, request))

# タブ（Tools）処理
def tools(request):
    return render(request,'tools.html')

# タブ（Master）処理
def master(request):
    return render(request,'master.html')

