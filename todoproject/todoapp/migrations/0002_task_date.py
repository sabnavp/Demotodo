# Generated by Django 3.2.14 on 2022-08-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2022-09-12'),
            preserve_default=False,
        ),
    ]
