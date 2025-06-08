"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('set_cookie_consent/', views.set_cookie_consent, name='set_cookie_consent'),
    path('all_the_options_view/', views.all_the_options_view, name='all_the_options_view'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('crear-propiedad/', views.create_property, name='create_property'),
    path('propiedades/<int:purpose_id>/<int:country_id>/', views.buscar_propiedades, name='buscar_propiedades'),
    path('contact/', views.contact, name='contact'),
    path('load-properties/', views.load_properties_ajax, name='load_properties_ajax'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('propiedad/<int:property_id>/reservar/', views.reservar_propiedad, name='reservar_propiedad'),
    path('buscar/<int:purpose_id>/<int:country_id>/', views.buscar_propiedades, name='buscar_propiedades'),





]
