# Generated by Django 4.1.6 on 2023-03-03 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0017_anott'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anof',
            old_name='TagifyCustomListSuggestion',
            new_name='tagify_options',
        ),
    ]