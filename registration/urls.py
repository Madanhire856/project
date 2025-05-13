from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
path('add_house/', views.add_house, name='add_house'),
    path('payments/', views.payments, name='payments'),
path('notices/', views.notices, name='notices'),
    path('post_notice/', views.post_notice,name='post_notice'),
path('display_payments/', views.display_payments,name='display_payments'),
path('admin_dashboard/', views.admin_dashboard,name='admin_dashboard'),
path('register/', views.register,name='register'),


]
