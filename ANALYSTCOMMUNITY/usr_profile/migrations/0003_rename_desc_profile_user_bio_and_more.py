# Generated by Django 5.0.6 on 2024-07-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr_profile', '0002_alter_profile_profile_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='desc',
            new_name='user_bio',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='title',
            new_name='user_designation',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_img',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_profile_image',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images'),
        ),
    ]
