# Generated by Django 5.1.4 on 2025-01-19 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_alter_booking_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='member',
            new_name='booking_member',
        ),
        migrations.AlterField(
            model_name='booking',
            name='fitness_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cls', to='gym.fitnessclass'),
        ),
    ]
