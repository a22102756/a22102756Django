# Generated by Django 4.2.2 on 2023-07-19 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0027_rename_projects_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Projects',
        ),
    ]
