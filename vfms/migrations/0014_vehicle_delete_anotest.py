# Generated by Django 4.1.6 on 2023-03-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0013_anotest_tagifycustomlistsuggestion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehi', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='anotest',
        ),
    ]