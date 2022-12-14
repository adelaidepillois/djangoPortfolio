# Generated by Django 3.2.15 on 2022-09-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_experience_date_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['id'], 'verbose_name': 'Expérience', 'verbose_name_plural': 'Expérience'},
        ),
        migrations.AddField(
            model_name='experience',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Ordre'),
            preserve_default=False,
        ),
    ]
