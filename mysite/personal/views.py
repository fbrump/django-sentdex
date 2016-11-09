# -*- coding:utf-8 -*-
# mysite/personal/views.py

from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')