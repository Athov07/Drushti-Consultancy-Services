# Generated by Django 5.0.6 on 2024-07-22 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_drushtiserplans', '0005_servicesplans_plan_condition1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plan_des_title', models.CharField(max_length=50)),
                ('Plan_Condition1', models.CharField(max_length=150)),
                ('Plan_Condition2', models.CharField(max_length=150)),
                ('Plan_Condition3', models.CharField(max_length=150)),
                ('Plan_Condition4', models.CharField(max_length=150)),
                ('Plan_Condition5', models.CharField(max_length=150)),
                ('close_btn', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='servicesplans',
            name='Plan_Condition1',
        ),
        migrations.RemoveField(
            model_name='servicesplans',
            name='Plan_Condition2',
        ),
        migrations.RemoveField(
            model_name='servicesplans',
            name='Plan_Condition3',
        ),
        migrations.RemoveField(
            model_name='servicesplans',
            name='Plan_Condition4',
        ),
        migrations.RemoveField(
            model_name='servicesplans',
            name='Plan_Condition5',
        ),
        migrations.RemoveField(
            model_name='servicesplans',
            name='Plan_des_title',
        ),
        migrations.RemoveField(
            model_name='servicesplans',
            name='close_btn',
        ),
    ]
