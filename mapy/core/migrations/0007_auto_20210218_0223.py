# Generated by Django 3.1.6 on 2021-02-18 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210218_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='artistText',
            field=models.TextField(max_length=1000),
        ),
    ]