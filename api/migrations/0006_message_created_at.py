# Generated by Django 3.2.8 on 2021-10-06 21:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_message_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
