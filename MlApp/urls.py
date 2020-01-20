from django.conf.urls import url
from . import views

urlpatterns = [
    # Url定義（index）
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),

    # Url定義（共通Tab）
#    url(r'^disptop$', views.top, name='disptop'),
    url(r'^tools$', views.tools, name='tools'),
    url(r'^master$', views.master, name='master'),

    # Url定義（top）
    url(r'^execution$', views.execution, name='execution'),
]