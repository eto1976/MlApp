from django.http.response import HttpResponse
from django.template import loader

from MlApp.batch.webCrawlerLogic import WebCrawlerLogic
from MlApp.forms.toolsform import ToolsForm


# 実行またはリロード処理
def toolsExecution(request):

    # 通常Form（※編集不可）
    form = ToolsForm(request.POST or None)
    # 編集用CopyForm
    formcopy = ToolsForm(request.POST.copy())

    url = form.data['sturlpath']
    msg = form.data['msg']

    #チェックボックスのリストの取得
    extensions = request.POST.getlist("fileExtension")

    # 実行ボタン押下時
    if 'doExecute' in request.POST and len(extensions)>0:
        # 画像クローリング処理
        msg = WebCrawlerLogic.crawring(url, extensions)
    elif len(extensions) == 0:
        msg = '拡張子を選択してください。'

    # メッセージをセット
    formcopy.data['msg'] = msg
    template = loader.get_template("tools.html")
    context = {
        "toolsForm": formcopy,
    }

    return HttpResponse(template.render(context, request))
