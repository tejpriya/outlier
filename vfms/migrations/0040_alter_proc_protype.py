# Generated by Django 4.1.6 on 2023-03-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0039_anott_processtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proc',
            name='protype',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
