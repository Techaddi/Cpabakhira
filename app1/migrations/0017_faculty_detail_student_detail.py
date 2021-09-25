# Generated by Django 3.2.3 on 2021-09-12 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0016_auto_20210912_0601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mother', models.CharField(max_length=100)),
                ('father', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=1000)),
                ('phone', models.CharField(max_length=100)),
                ('standerd', models.CharField(max_length=100)),
                ('aadhar', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('pre_standerd', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='assets')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=1000)),
                ('father', models.CharField(max_length=100)),
                ('aadhar', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='assets')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
