# Generated by Django 3.2.11 on 2022-01-31 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='assignee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='information',
            name='type',
            field=models.CharField(choices=[('B', 'Bug'), ('P', 'Phase'), ('T', 'Task'), ('U', 'User story')], max_length=255),
        ),
    ]
