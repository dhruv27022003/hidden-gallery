from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("view", views.show_file, name='view'),
    path("?username=12345678", views.inn, name="inn"),
    path("hiden", views.hiden, name='hiden'),
        path('inde', views.inde, name="inde"),
     path('create', views.create, name="create"),
    path('login', views.logi, name="logi"),
    path('logout', views.logou, name="logou"),
  #  path("about", views.about, name='home'),
  #  path("services", views.services, name='home'),
  #   path("contact", views.contact, name='home'),
  #     path("tea", views.tea, name='home')
   
]
