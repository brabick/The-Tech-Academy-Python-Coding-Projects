from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    #sets the homepage to views.home
    #path('', views.home, name = 'home'),
    path('admin_console', views.admin_console, name = 'admin_console'),
    path('<int:pk>/details/', views.details, name = 'details'),
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    path('confirmDelete/', views.confirmed, name = 'confirmed'),
    path('createRecord/', views.createRecord, name='createRecord'),
    ]