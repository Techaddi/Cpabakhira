# Generated by Django 3.2.3 on 2021-09-04 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_faculties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculties',
            name='about',
            field=models.TextField(max_length=500),
        ),
    ]
