# Generated by Django 3.0.6 on 2020-06-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20200610_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='submission_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
