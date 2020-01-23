from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url


app_name='aj_web'
urlpatterns = [
    path('', views.MainView.as_view(), name='home'),

]


