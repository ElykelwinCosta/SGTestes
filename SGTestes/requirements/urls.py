from django.urls import path
from . import views

urlpatterns = [
    # Defina suas rotas aqui, por exemplo:
    path('requirement_list/', views.requirement_list, name='requirement_list'),
    # Outras rotas do aplicativo 'requirements'
]
