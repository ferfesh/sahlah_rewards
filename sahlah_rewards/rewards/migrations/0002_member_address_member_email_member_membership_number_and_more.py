# Generated by Django 5.0.6 on 2024-06-02 20:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='member',
            name='membership_number',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='member',
            name='national_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='member',
            name='upline_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='upline_number',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='member',
            name='referral_code',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
