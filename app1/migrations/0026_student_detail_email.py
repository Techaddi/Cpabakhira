# Generated by Django 3.2.4 on 2021-09-20 12:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_student_detail_fee_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_detail',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]