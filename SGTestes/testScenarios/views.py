from django.shortcuts import render
from .models import TestScenario

def scenario_list(request):
    scenarios = TestScenario.objects.all()
    # Lógica para exibir a lista de cenários de teste
    return render(request, 'testScenarios/scenario_list.html', {'scenarios': scenarios})

# Adicione outras views para adicionar, editar, excluir cenários, etc.
