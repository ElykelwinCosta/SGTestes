from django.urls import path
from . import views

urlpatterns = [
    # Defina suas rotas aqui
    path('reports/', views.view_report, name='view_report'),
    # Outras rotas do aplicativo 'reports'
]
