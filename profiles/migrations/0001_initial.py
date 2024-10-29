# Generated by Django 5.1.2 on 2024-10-29 19:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=20, null=True, verbose_name='First Name')),
                ('lastname', models.CharField(blank=True, max_length=20, null=True, verbose_name='Last Name')),
                ('mobile', models.CharField(blank=True, max_length=12, null=True, verbose_name='mobile phone')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
