# Generated by Django 4.1.6 on 2023-03-04 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0019_tag_delete_anott_anof_tagify_vehicle_tagify'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anof',
            name='tagify_options',
        ),
    ]
