# Generated by Django 4.0.6 on 2023-03-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mikvah', '0005_appointment_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
