# Generated by Django 5.0.6 on 2024-08-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='explore_more',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_slid_img', models.FileField(blank=True, max_length=250, null=True, upload_to='explore_more/')),
            ],
        ),
    ]
