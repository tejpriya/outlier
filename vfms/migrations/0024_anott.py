# Generated by Django 4.1.6 on 2023-03-06 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0023_alter_anof_vehi'),
    ]

    operations = [
        migrations.CreateModel(
            name='anott',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vfms.vehicle')),
            ],
        ),
    ]
