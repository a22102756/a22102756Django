# Generated by Django 4.2.2 on 2023-07-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_alter_noticia_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='deslikes',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
