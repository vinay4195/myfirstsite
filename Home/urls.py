from django.contrib import admin
from django.urls import path, include
from Home import views
urlpatterns = [
   path('', views.home , name='home'),
   path('myfirstsite/about', views.about , name='about'),
   path('myfirstsite/project', views.project , name='project'),
   path('myfirstsite/contact', views.contact , name='contact')
   
]
