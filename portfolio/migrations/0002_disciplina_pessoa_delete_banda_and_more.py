# Generated by Django 4.2.2 on 2023-07-02 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('ECTS', models.IntegerField()),
                ('ano_letivo', models.IntegerField()),
                ('topicos_abordados', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Banda',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplina', to='portfolio.pessoa'),
        ),
    ]
