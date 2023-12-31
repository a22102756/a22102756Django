# Generated by Django 4.2.2 on 2023-07-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0025_post_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('ano', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_images/')),
                ('resumo', models.CharField(max_length=500)),
                ('report_link', models.URLField(blank=True)),
                ('github_repo', models.URLField(blank=True)),
                ('advisors', models.ManyToManyField(related_name='projects', to='portfolio.advisor')),
                ('autor', models.ManyToManyField(related_name='projects', to='portfolio.author')),
            ],
        ),
    ]
