# Generated by Django 5.0.6 on 2024-06-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0004_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_files',
            field=models.ManyToManyField(related_name='project', to='management_app.projectfile'),
        ),
    ]