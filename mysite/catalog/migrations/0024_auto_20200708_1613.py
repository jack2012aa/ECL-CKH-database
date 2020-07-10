# Generated by Django 3.0.3 on 2020-07-08 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_auto_20200706_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='pig',
            name='registration_number',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='pig_history',
            name='registration_number',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='data_id',
            field=models.CharField(max_length=17, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='data_history',
            name='data_id',
            field=models.CharField(max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='pig',
            name='breed',
            field=models.CharField(choices=[('L', 'Landrace'), ('Y', 'Yorkshire'), ('D', 'Duroc')], help_text="Pig's breed", max_length=10),
        ),
        migrations.AlterField(
            model_name='pig',
            name='pig_id',
            field=models.CharField(help_text='Input birth year(XX) + ear tag', max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pig_depth_video',
            name='video_id',
            field=models.CharField(max_length=17, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pig_history',
            name='pig_id',
            field=models.CharField(help_text='Input birth year(XX) + ear tag', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='pig_video',
            name='video_id',
            field=models.CharField(max_length=17, primary_key=True, serialize=False),
        ),
    ]
