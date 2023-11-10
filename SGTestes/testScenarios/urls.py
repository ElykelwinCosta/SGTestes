from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.scenario_list, name='scenario_list'),
    # Adicione outras rotas conforme necessário
]
