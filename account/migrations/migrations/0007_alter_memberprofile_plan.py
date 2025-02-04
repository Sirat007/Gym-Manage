# Generated by Django 5.1.4 on 2025-01-25 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_memberprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberprofile',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plans', to='account.gymplan'),
        ),
    ]
