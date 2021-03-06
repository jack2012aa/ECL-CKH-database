# Generated by Django 3.0.5 on 2020-05-21 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20200519_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pig_history',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Data_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.IntegerField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('length', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('front_width', models.FloatField(null=True)),
                ('back_width', models.FloatField(null=True)),
                ('depth', models.FloatField(null=True)),
                ('chest', models.FloatField(null=True)),
                ('front_cannon_circumference', models.FloatField(null=True)),
                ('back_cannon_circumference', models.FloatField(null=True)),
                ('date', models.DateField(null=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('pig_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Pig')),
            ],
        ),
    ]
