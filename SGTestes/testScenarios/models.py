from django.db import models
from users.models import CustomUser
from requirements.models import Requirement

class TestScenario(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)

    # Adicione aqui outros campos necessários para os cenários de teste
