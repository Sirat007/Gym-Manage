# Generated by Django 5.1.4 on 2025-02-02 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_memberprofile_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberprofile',
            name='plan',
        ),
    ]
