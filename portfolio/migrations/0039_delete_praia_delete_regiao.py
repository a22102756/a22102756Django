# Generated by Django 4.2.2 on 2023-07-19 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0038_remove_regiao_praia_praia_regiao'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Praia',
        ),
        migrations.DeleteModel(
            name='Regiao',
        ),
    ]
