# Generated by Django 5.0.7 on 2024-09-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='role',
            field=models.CharField(default='Student', max_length=10),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='role',
            field=models.CharField(default='Teacher', max_length=10),
        ),
    ]