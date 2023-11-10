from django.urls import path
from . import views

urlpatterns = [
    # Defina suas rotas aqui
    path('dashboard/', views.dashboard, name='dashboard'),
    # Outras rotas do aplicativo 'dashboards'
]