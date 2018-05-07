from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns =[
		path('dashboard',views.home, name="home"),
		path('dashboard/new_room', views.new_room, name="new_room"),
		]