# Generated by Django 3.0.3 on 2020-06-01 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20200529_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pig_Video',
            fields=[
                ('video_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('video', models.FileField(upload_to='pig_video')),
                ('photographer', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('camera', models.CharField(max_length=40)),
                ('pig_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Pig')),
            ],
        ),
    ]