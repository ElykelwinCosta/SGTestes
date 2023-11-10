from django.shortcuts import render
from .models import TestScenario

def dashboard(request):
    # Suponha que 'TestScenario' é o modelo que possui os cenários de teste
    test_scenarios = TestScenario.objects.all()  # Recupera todos os cenários de teste

    context = {
        'test_scenarios': test_scenarios  # Passa os cenários de teste para o contexto do template
        # Adicione mais dados que você deseja exibir no dashboard
    }

    return render(request, 'dashboards/dashboard.html', context)
