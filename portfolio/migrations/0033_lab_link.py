# Generated by Django 4.2.2 on 2023-07-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0032_lab'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
