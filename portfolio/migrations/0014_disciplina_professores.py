# Generated by Django 4.2.2 on 2023-07-16 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_remove_post_comentario_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='professores',
            field=models.ManyToManyField(related_name='disciplina', to='portfolio.pessoa'),
        ),
    ]
