# Generated by Django 3.2.8 on 2021-10-06 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_message_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='myMessages',
            field=models.ManyToManyField(blank=True, null=True, to='api.Message'),
        ),
    ]
