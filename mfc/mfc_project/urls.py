from django.contrib import admin
from django.urls import path, include
from .views import index, treatment,thsDo, thsPosle

urlpatterns = [
    path('', index),
    path('treatment', treatment, name="treatment"),
    path('thsDo', thsDo, name="thsDo"),
    path('thsPosle', thsPosle, name="thsPosle"),

]
