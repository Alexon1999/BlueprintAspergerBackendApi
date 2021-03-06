# Generated by Django 3.2.8 on 2021-10-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.CharField(max_length=30)),
                ('destinataireId', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='myMessages',
            field=models.ManyToManyField(to='api.Message'),
        ),
    ]
