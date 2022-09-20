# Generated by Django 3.2.15 on 2022-09-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_experience_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Ordre')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('category', models.CharField(choices=[('IN', 'Informatique'), ('TH', 'Théorique'), ('ST', 'Soft-Skills')], default='IN', max_length=2, verbose_name='Section')),
                ('title', models.CharField(max_length=255, verbose_name="Nom de l'expérience")),
                ('logo', models.ImageField(default='logo', upload_to='', verbose_name="Logo de l'expérience")),
                ('is_active', models.BooleanField(verbose_name='Expérience active')),
            ],
            options={
                'verbose_name': 'Expérience',
                'verbose_name_plural': 'Expérience',
                'ordering': ['order'],
            },
        ),
    ]