# Generated by Django 3.0.5 on 2020-04-14 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20200414_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='data_id',
            field=models.CharField(help_text='Input date + pig_id', max_length=11, null=True),
        ),
    ]