# Generated by Django 5.1.4 on 2025-02-03 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_rename_plan_planadd_planadded_memberprofile_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
