from django.conf.urls import url
from django.contrib import admin
from django.urls import path

import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # url(r'^xadmin/', xadmin.site.urls),
]
