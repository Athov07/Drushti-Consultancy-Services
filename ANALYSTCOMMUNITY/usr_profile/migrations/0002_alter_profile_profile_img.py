# Generated by Django 5.0.6 on 2024-07-24 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='/media/images/default.jpg', null=True, upload_to='images'),
        ),
    ]
