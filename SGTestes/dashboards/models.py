from django.db import models

class TestScenario(models.Model):
    # Definição dos campos do modelo TestScenario
    scenario_name = models.CharField(max_length=100)
    description = models.TextField()
    # Outros campos necessários para descrever um cenário de teste

    def __str__(self):
        return self.scenario_name  # Retorna o nome do cenário como representação em string
