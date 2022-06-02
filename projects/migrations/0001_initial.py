# Generated by Django 4.0.4 on 2022-06-01 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1023)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
