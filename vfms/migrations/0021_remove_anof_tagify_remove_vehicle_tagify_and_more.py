# Generated by Django 4.1.6 on 2023-03-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0020_remove_anof_tagify_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anof',
            name='tagify',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='tagify',
        ),
        migrations.AddField(
            model_name='anof',
            name='TagifyCustomListSuggestion',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='tag',
        ),
    ]
