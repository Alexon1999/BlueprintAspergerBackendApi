# Generated by Django 3.2.8 on 2021-10-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=320)),
                ('password', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=15)),
                ('statut', models.CharField(max_length=15)),
            ],
        ),
    ]
