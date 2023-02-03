# Generated by Django 4.0.6 on 2023-04-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mikvah', '0006_appointment_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayconfiguration',
            name='first_come_first_served',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]
