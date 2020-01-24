from django.http.response import HttpResponse
from django.template import loader

from MlApp.forms.topform import TopForm
from MlApp.models.mstimagelabel import Mst_imagelabel
from MlApp.forms.toolsform import ToolsForm


# タブ（Top）処理
def tabmenuTop(request):

    topform = TopForm()
    # プルダウン初期値追加のカテゴリー1のみ追加
    # カテゴリー1
    imagelabel_ct1 = []
    CATEGORIES_1 = ()

    for objimagelabel in Mst_imagelabel.objects.filter(baselabelclass__isnull=True):
        imagelabel_ct1.append(objimagelabel)

    for imagelabel_ct1_obj in imagelabel_ct1:
        CATEGORIES_1_GET = (
            (imagelabel_ct1_obj.labelclass, imagelabel_ct1_obj.labelclassname),
        )

        CATEGORIES_1 = CATEGORIES_1 + CATEGORIES_1_GET

    # 選択肢追加
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
def tabmenuTools(request):

    toolsForm = ToolsForm()
    template = loader.get_template("tools.html")
    context = {
        "toolsForm": toolsForm,
    }

    return HttpResponse(template.render(context, request))

# タブ（Master）処理
def tabmenuMaster(request):

    template = loader.get_template("master.html")
    context = {

    }

    return HttpResponse(template.render(context, request))

