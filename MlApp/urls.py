from django.conf.urls import url
from . import views

urlpatterns = [
    # Url定義（index）
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),

    # Url定義（top）
    url(r'^top$', views.top, name='top'),
    url(r'^master$', views.master, name='master'),
    url(r'^execution$', views.execution, name='execution'),
]