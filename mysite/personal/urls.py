# -*- coding:utf-8 -*-
# mysite/personal/urls.py

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
