# Generated by Django 5.0.3 on 2024-03-17 09:20

from django.db import migrations
from django.contrib.postgres.operations import CreateExtension


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        CreateExtension("pg_trgm")
    ]