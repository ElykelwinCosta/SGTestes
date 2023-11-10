from django.shortcuts import render
from .models import Requirement

def requirement_list(request):
    requirements = Requirement.objects.all()
    # Lógica para exibir a lista de requisitos
    return render(request, 'requirements/requirement_list.html', {'requirements': requirements})

# Adicione outras views para adicionar, editar, excluir requisitos, etc.
