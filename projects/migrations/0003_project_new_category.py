# Generated by Django 5.0 on 2024-01-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='new_category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
