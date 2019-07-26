from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import views
urlpatterns = [
    re_path(r'^genero/$', views.GeneroList.as_view()),
    re_path(r'^genero/(?P<pk>\d+)$', views.GeneroDetail.as_view()),
    
    re_path(r'^ciudad/$', views.CiudadList.as_view()),
    re_path(r'^ciudad/(?P<pk>\d+)$', views.CiudadDetail.as_view()),
    
    re_path(r'^estado/$', views.EstadoList.as_view()),
    re_path(r'^estado/(?P<pk>\d+)$', views.EstadoDetail.as_view()),
    
    re_path(r'^civil/$', views.CivilList.as_view()),
    re_path(r'^civil/(?P<pk>\d+)$', views.CivilDetail.as_view()),
]