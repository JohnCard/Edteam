# Generated by Django 4.2.7 on 2023-12-11 20:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coursera', '0014_alter_course_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='modules',
            field=models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
    ]
