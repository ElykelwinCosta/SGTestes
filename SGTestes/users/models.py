from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('qa', 'QA'),
        ('leader', 'Líder')
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    class Meta:
        app_label = 'users'

    groups = models.ManyToManyField(Group, related_name='custom_user')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user')
