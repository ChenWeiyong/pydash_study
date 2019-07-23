"""pydash_study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views
from django.conf import settings
from django.views import static
from django.conf.urls import url
from django.urls import re_path

urlpatterns = [
    path('', views.index),
    path('info/getdisk/', views.getdisk, name="getdisk"),
    path('info/getnetstat/', views.getnetstat, name="getnetstat"),
    path('info/uptime/', views.uptime, name="uptime"),
    path('info/memory/', views.memusage, name="memusage"),
    path('info/cpuusage/', views.cpuusage, name="cpuusage"),
    path('info/getusers/', views.getusers, name="getusers"),
    path('info/getips/', views.getips, name="getips"),
    path('info/gettraffic/', views.gettraffic, name="gettraffic"),
    path('info/proc/', views.getproc, name="getproc"),
    path('info/getdiskio/', views.getdiskio, name="getdiskio"),
    path('info/loadaverage/', views.loadaverage, name="loadaverage"),
    # re_path(r'^info/platform/([\w\-\.]+)/$', views.plat_form),
    # re_path(r'^info/getcpus/([\w\-\.]+)/$', views.getcpus),
    path('info/platform/<str:name>/', views.plat_form),
    path('info/getcpus/<str:name>/', views.getcpus),

    re_path(r'^static/(?P<path>.*)$', static.serve,
            {'document_root': settings.STATIC_ROOT}, name='static')
]
