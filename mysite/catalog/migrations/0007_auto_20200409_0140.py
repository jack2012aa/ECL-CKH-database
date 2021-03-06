# Generated by Django 3.0.3 on 2020-04-08 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20200409_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='pig',
        ),
        migrations.RemoveField(
            model_name='pig',
            name='breed',
        ),
        migrations.AddField(
            model_name='data',
            name='pig_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Pig'),
        ),
        migrations.AddField(
            model_name='pig',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='catalog.Genre'),
        ),
    ]
