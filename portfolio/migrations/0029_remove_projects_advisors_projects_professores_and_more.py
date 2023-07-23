# Generated by Django 4.2.2 on 2023-07-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0028_rename_project_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='advisors',
        ),
        migrations.AddField(
            model_name='projects',
            name='professores',
            field=models.ManyToManyField(related_name='projects', to='portfolio.pessoa'),
        ),
        migrations.DeleteModel(
            name='Advisor',
        ),
    ]