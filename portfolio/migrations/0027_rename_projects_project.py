# Generated by Django 4.2.2 on 2023-07-19 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0026_advisor_author_projects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]