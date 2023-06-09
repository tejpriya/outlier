# Generated by Django 4.1.6 on 2023-03-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfms', '0012_anotest'),
    ]

    operations = [
        migrations.AddField(
            model_name='anotest',
            name='TagifyCustomListSuggestion',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anotest',
            name='vehicles',
            field=models.CharField(choices=[('bus', 'bus'), ('car', 'car'), ('truck', 'truck'), ('minibus', 'minibus'), ('multiaxle', 'multiaxle'), ('2axle', '2axle'), ('3axle', '3axle'), ('4axle', '4axle'), ('earth mover', 'earth mover'), ('autorickshaw', 'autorickshaw'), ('lcv', 'lcv')], max_length=200, null=True),
        ),
    ]
