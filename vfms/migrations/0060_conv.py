# Generated by Django 4.1.6 on 2023-03-21 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0059_alter_dups_dropzone'),
    ]

    operations = [
        migrations.CreateModel(
            name='conv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml_dir', models.CharField(max_length=300)),
            ],
        ),
    ]