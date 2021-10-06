from django.db import models
from django.utils import timezone

# Create your models here.


class Message(models.Model):
    contenu = models.TextField()
    destinataireId = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.contenu + " " + str(self.destinataireId)


class Utilisateur(models.Model):
    nom = models.CharField(max_length=30, null=False)
    prenom = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=320, null=False)
    password = models.CharField(max_length=30, null=False)
    tel = models.CharField(max_length=15)

    status_choices = [
        ("patient", 'patient'),
        ("medecin", 'medecin'),
    ]
    statut = models.CharField(max_length=15,
                              choices=status_choices,
                              default="patient")

    myMessages = models.ManyToManyField(Message, blank=True, null=True)

    def __str__(self):
        return self.nom + " " + self.prenom + " " + str(self.id)
