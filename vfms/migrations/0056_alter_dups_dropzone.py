# Generated by Django 4.1.6 on 2023-03-18 06:55

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0055_remove_dups_uploade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dups',
            name='dropzone',
            field=models.FileField(null=True, storage=django.core.files.storage.FileSystemStorage(location='E:\\drive'), upload_to='Uploaded/'),
        ),
    ]
