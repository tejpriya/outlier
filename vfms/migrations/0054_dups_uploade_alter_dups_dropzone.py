# Generated by Django 4.1.6 on 2023-03-18 06:53

import django.core.files.storage
from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0053_remove_dups_destination_folder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dups',
            name='uploade',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now().isoformat()),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dups',
            name='dropzone',
            field=models.FileField(null=True, storage=django.core.files.storage.FileSystemStorage(location='E:\\drive'), upload_to='Uploaded/%Y/%m/%d/'),
        ),
    ]