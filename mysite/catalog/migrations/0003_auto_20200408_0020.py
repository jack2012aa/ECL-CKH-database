# Generated by Django 3.0.3 on 2020-04-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200407_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.URLField(blank=True),
        ),
    ]