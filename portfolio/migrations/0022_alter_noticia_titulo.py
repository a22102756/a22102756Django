# Generated by Django 4.2.2 on 2023-07-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_delete_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]