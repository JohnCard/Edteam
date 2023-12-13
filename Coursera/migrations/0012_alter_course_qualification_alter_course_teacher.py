# Generated by Django 4.2 on 2023-11-23 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coursera', '0011_alter_course_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='qualification',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.CharField(choices=[('opt 1', 'Álvaro Felipe'), ('opt 2', 'Beto Quiroga'), ('opt 3', 'Alexys Lozada'), ('opt 4', 'Johnny'), ('opt 5', 'Queta Rodriguez'), ('opt 6', 'Oscar Alzada')], max_length=30),
        ),
    ]
