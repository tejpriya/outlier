# Generated by Django 4.1.6 on 2023-03-18 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0054_dups_uploade_alter_dups_dropzone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dups',
            name='uploade',
        ),
    ]