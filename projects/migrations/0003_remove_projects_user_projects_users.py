# Generated by Django 4.0.4 on 2022-06-02 12:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_alter_projects_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='user',
        ),
        migrations.AddField(
            model_name='projects',
            name='users',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
