# Generated by Django 4.1.6 on 2023-03-22 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0066_rename_root_dir_conv_myroot_dir'),
    ]

    operations = [
        migrations.AddField(
            model_name='conv',
            name='txt_dir',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]