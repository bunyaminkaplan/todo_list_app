# Generated by Django 5.0.3 on 2024-04-26 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0004_mission_remained_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='username',
            field=models.CharField(default='non-qualified', max_length=20),
        ),
    ]
