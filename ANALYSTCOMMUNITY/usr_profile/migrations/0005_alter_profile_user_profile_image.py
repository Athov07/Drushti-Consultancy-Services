# Generated by Django 5.0.6 on 2024-09-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr_profile', '0004_alter_profile_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_profile_image',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images'),
        ),
    ]
