# Generated by Django 4.2.7 on 2023-11-04 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('requirements', '0001_initial'),
        ('testScenarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testscenario',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
        ),
        migrations.AddField(
            model_name='testscenario',
            name='requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requirements.requirement'),
        ),
    ]
