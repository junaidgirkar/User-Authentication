# Generated by Django 3.0.8 on 2020-09-03 12:25

import classroom.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20200903_1747'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student',
            managers=[
                ('objects', classroom.managers.StudentManager()),
            ],
        ),
    ]
