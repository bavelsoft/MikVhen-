# Generated by Django 4.0.6 on 2023-03-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mikvah', '0004_dayconfiguration'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='payment',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
