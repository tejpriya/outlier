# Generated by Django 4.1.6 on 2023-03-08 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0028_anott_op_alter_anott_vehi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anott',
            old_name='vehi',
            new_name='vehic',
        ),
    ]
