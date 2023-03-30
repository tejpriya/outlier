# Generated by Django 4.1.6 on 2023-03-09 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0040_alter_proc_protype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anott',
            name='processtype',
            field=models.CharField(choices=[('add-id', 'Add ID'), ('rename', 'Rename'), ('crop', 'Crop'), ('remove-id', 'Remove ID')], max_length=10),
        ),
    ]
