# Generated by Django 3.0.5 on 2020-05-19 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20200505_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pig_history',
            fields=[
                ('pig_id', models.CharField(help_text='Input birth year(XX) + ear tag', max_length=8, primary_key=True, serialize=False)),
                ('birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('dad_id', models.CharField(max_length=100, null=True)),
                ('mom_id', models.CharField(max_length=100, null=True)),
                ('breed', models.CharField(blank=True, help_text="Pig's breed", max_length=10, null=True)),
                ('modified_date', models.TimeField()),
            ],
        ),
    ]
