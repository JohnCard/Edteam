# Generated by Django 4.2 on 2023-11-18 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('qualification', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('teacher', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
