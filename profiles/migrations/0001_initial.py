# Generated by Django 3.1.3 on 2021-04-21 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('default_last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('default_username', models.CharField(blank=True, max_length=20, null=True)),
                ('default_email', models.CharField(blank=True, max_length=80, null=True)),
                ('default_password', models.CharField(blank=True, max_length=40, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
