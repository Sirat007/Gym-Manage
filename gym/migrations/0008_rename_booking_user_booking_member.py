# Generated by Django 5.1.4 on 2025-01-19 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_rename_booking_member_booking_booking_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_user',
            new_name='member',
        ),
    ]
