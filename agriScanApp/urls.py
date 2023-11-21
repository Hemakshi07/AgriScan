
from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'agriScanApp'

urlpatterns = [
    # path('login/', views.LoginView, name='login'),
    path('', views.dashboard, name='dashboard'),
    # path('aboutus/', views.aboutus, name='aboutus'),
    # path('contactus/', views.contactus, name='contactus'),
    # path('services/', views.services, name='services'),
    path('login/', views.login_view, name='login'),
    path('register/', views.registration, name='registration'),
    path('home/', views.home, name='home')
]
