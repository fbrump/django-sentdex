# -*- coding:utf-8 -*-
# mysite/blog/admin.py

from django.contrib import admin
from blog.models import Post

admin.site.register(Post)
