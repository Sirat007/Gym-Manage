# Generated by Django 5.1.4 on 2025-01-19 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_alter_booking_booking_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_member',
            new_name='booking_user',
        ),
    ]
