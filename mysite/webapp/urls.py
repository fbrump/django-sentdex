# -*- coding:utf-8 -*-
# mysite/webapp/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
