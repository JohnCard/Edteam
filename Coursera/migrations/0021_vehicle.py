# Generated by Django 4.2.7 on 2024-05-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coursera', '0020_remove_course_date_course_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=35)),
                ('plaque', models.CharField(max_length=20)),
                ('vin', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('sub_brand', models.CharField(max_length=20)),
                ('verify_reason', models.CharField(max_length=30)),
                ('service', models.CharField(max_length=15)),
                ('line', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('no_tech', models.IntegerField()),
                ('folio', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
