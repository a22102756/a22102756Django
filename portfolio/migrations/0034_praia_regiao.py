# Generated by Django 4.2.2 on 2023-07-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0033_lab_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Praia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('praia', models.ManyToManyField(related_name='regiao', to='portfolio.praia')),
            ],
        ),
    ]
