# Generated by Django 4.1.6 on 2023-03-08 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0035_anof_unique_anof_tags'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='anof',
            name='unique_anof_tags',
        ),
    ]
