from django.shortcuts import render
from .models import TestReport

def view_report(request, report_id):
    report = TestReport.objects.get(id=report_id)
    # Lógica para exibir um relatório específico
    return render(request, 'reports/view_report.html', {'report': report})

# Adicione outras views para gerar relatórios, adicionar comentários, aprovar/reprovar cenários, etc.
