# Generated by Django 4.1.6 on 2023-03-21 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0064_rename_dups_clus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clus',
            old_name='cropped_images_path',
            new_name='mov_dir',
        ),
        migrations.RenameField(
            model_name='clus',
            old_name='moving_path',
            new_name='root_dir',
        ),
    ]
