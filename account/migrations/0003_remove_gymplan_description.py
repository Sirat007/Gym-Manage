# Generated by Django 5.1.4 on 2025-01-15 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_gymplan_alter_customuser_user_type_memberprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gymplan',
            name='description',
        ),
    ]
