# Generated by Django 3.2.8 on 2021-10-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_utilisateur_mymessages'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='contenu',
            field=models.TextField(),
        ),
    ]
