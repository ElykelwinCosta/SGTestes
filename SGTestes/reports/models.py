from django.db import models
from testScenarios.models import TestScenario
from users.models import CustomUser

class TestReport(models.Model):
    test_scenario = models.ForeignKey(TestScenario, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    approved = models.BooleanField()
    # Adicione campos para data, hora, ou outros detalhes que considerar necessário
