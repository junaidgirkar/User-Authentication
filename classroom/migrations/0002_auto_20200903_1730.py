# Generated by Django 3.0.8 on 2020-09-03 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='default', max_length=255, unique=True, verbose_name='username'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='username',
            field=models.CharField(default='default', max_length=255, unique=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='default', max_length=255, unique=True, verbose_name='username'),
        ),
    ]