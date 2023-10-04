
from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'agriScanApp'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    # path('login/', views.LoginView, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
   

]
