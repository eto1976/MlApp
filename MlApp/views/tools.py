from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from MlApp.batch.webCrawlerLogic import WebCrawlerLogic
from MlApp.forms.toolsform import ToolsForm


# 実行またはリロード処理
def toolsExecution(request):

    #通常Form（※編集不可）
    form = ToolsForm(request.POST or None)
    #編集用CopyForm
    formcopy = ToolsForm(request.POST.copy())

    url = form.data['sturlpath']
    extensions = form.data['fileExtension']

    # 実行ボタン押下時
    if 'doExecute' in request.POST:

        # 画像クローリング処理
        msg = WebCrawlerLogic.crawring(url, extensions)


    #メッセージをセット
    formcopy.data['msg'] = msg
    template = loader.get_template("tools.html")
    context = {
        "toolsform": formcopy,
    }

    return HttpResponse(template.render(context, request))
