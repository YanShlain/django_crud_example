# Generated by Django 3.1.7 on 2021-03-10 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Worker',
        ),
    ]