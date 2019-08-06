from django.contrib import admin
from django.urls import include, path
from . import views 

app_name = 'static_website'
urlpatterns = [
    path('', views.Home.as_view(), name='index'),
]
