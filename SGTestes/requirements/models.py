from django.db import models

class Requirement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    redmine_id = models.IntegerField()  # Exemplo de campo para armazenar o ID do Redmine

    # Adicione outros campos conforme necessário para representar os requisitos
