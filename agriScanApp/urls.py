
from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'agriScanApp'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.registration, name='registration'),
    path('home/', views.home, name='home'),
    path('get_user_details/', views.get_user_details, name='get_user_details'),
    path('charts/', views.chartsView, name='charts')
]
