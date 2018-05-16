from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns =[
		path(r'',views.profile, name="profile"),
		# path('dashboard/new_room', views.new_room, name="new_room"),
		]