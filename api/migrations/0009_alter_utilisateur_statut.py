# Generated by Django 3.2.8 on 2021-10-06 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_mail_utilisateur_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='statut',
            field=models.CharField(choices=[('patient', 'patient'), ('medecin', 'medecin')], default='patient', max_length=15),
        ),
    ]
