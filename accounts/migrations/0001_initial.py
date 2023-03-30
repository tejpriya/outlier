# Generated by Django 4.1.6 on 2023-02-28 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50)),
                ('role_description', models.CharField(max_length=200)),
                ('role_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
                ('user_name', models.CharField(max_length=60, null=True)),
                ('user_email', models.CharField(max_length=100, null=True)),
                ('user_mobile', models.CharField(max_length=15, null=True)),
                ('user_image_url', models.CharField(max_length=500, null=True)),
                ('user_social_provider', models.CharField(max_length=50, null=True)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('user_status', models.BooleanField(default=True)),
                ('user_company_name', models.CharField(max_length=100, null=True)),
                ('user_business_type', models.CharField(max_length=100, null=True)),
                ('user_description', models.CharField(max_length=200, null=True)),
                ('user_country', models.CharField(max_length=50, null=True)),
                ('user_state', models.CharField(max_length=50, null=True)),
                ('user_city', models.CharField(max_length=50, null=True)),
                ('user_roles', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.roles')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('user_name', models.CharField(max_length=60)),
                ('user_email', models.CharField(max_length=100)),
                ('user_mobile', models.CharField(max_length=15, null=True)),
                ('user_password', models.CharField(max_length=20, null=True)),
                ('user_company_name', models.CharField(max_length=100, null=True)),
                ('user_business_type', models.CharField(max_length=100, null=True)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('user_status', models.BooleanField(default=True)),
                ('user_image', models.ImageField(blank=True, upload_to='profile_image')),
                ('user_description', models.CharField(max_length=200, null=True)),
                ('user_country', models.CharField(max_length=50, null=True)),
                ('user_state', models.CharField(max_length=50, null=True)),
                ('user_city', models.CharField(max_length=50, null=True)),
                ('user_image_url', models.CharField(max_length=500, null=True)),
                ('user_social_provider', models.CharField(max_length=50, null=True)),
                ('user_profile_update', models.DateField(auto_now_add=True, null=True)),
                ('pre_last_login', models.DateTimeField(auto_now_add=True)),
                ('user_roles', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.roles')),
            ],
        ),
    ]
