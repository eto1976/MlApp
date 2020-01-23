from django.conf.urls import url
from . import views

urlpatterns = [
    # Url定義（index）ログイン後のIndex画面に戻るURLも定義
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),

    # Url定義（共通Tab）
    url(r'^tabmenuTop$', views.tabmenuTop, name='tabmenuTop'),
    url(r'^tabmenuTools$', views.tabmenuTools, name='tabmenuTools'),
    url(r'^tabmenuMaster$', views.tabmenuMaster, name='tabmenuMaster'),

    # Url定義（top）
    url(r'^topExecution', views.topExecution, name='topExecution'),

    # Url定義（tools）
    url(r'^toolsExecution', views.toolsExecution, name='toolsExecution'),

]