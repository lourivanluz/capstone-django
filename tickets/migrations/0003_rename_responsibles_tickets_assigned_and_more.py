# Generated by Django 4.0.4 on 2022-06-02 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_projects_user_projects_users'),
        ('tickets', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tickets',
            old_name='responsibles',
            new_name='assigned',
        ),
        migrations.AlterField(
            model_name='tickets',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='projects.projects'),
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
