# Generated by Django 4.2.7 on 2024-01-26 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTube', '0002_video_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='icon',
            field=models.ImageField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.PositiveBigIntegerField(default=10000),
        ),
        migrations.AddField(
            model_name='video',
            name='youtuber',
            field=models.CharField(default='Developer avenger', max_length=70),
        ),
    ]
