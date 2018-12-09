from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^top$', views.top, name='top'),
    url(r'^work$', views.work, name='work'),
    url(r'^execution$', views.execution, name='execution'),
]