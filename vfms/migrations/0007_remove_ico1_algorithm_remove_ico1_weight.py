# Generated by Django 4.1.6 on 2023-03-01 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0006_ico1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ico1',
            name='Algorithm',
        ),
        migrations.RemoveField(
            model_name='ico1',
            name='Weight',
        ),
    ]
