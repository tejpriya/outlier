# Generated by Django 4.1.6 on 2023-03-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0062_rename_txt_dir_conv_root_dir_remove_conv_xml_dir'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dups',
            name='dropzone',
        ),
        migrations.AddField(
            model_name='dups',
            name='cropped_images_path',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dups',
            name='moving_path',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]