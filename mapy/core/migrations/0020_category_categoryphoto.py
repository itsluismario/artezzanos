# Generated by Django 3.1.7 on 2021-03-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20210320_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='categoryPhoto',
            field=models.FileField(default=1, upload_to='categories'),
            preserve_default=False,
        ),
    ]