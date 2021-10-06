from rest_framework import serializers
from .models import *


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id",
                  "contenu",
                  "destinataireId",
                  ]


class MessageUtilisateurSerializer(serializers.ModelSerializer):
    # destinataire = serializers.SerializerMethodField('get_destinataire')

    # def get_destinataire(self, message):
    #     qs = Utilisateur.objects.get(id=message.destinataireId)
    #     serializer = UtilisateurSerializer(instance=qs)
    #     return serializer.data

    class Meta:
        model = Message
        fields = ["id",
                  "contenu",
                  "destinataireId",
                  ]


class UtilisateurSerializer(serializers.ModelSerializer):
    myMessages = MessageUtilisateurSerializer(many=True)

    class Meta:
        model = Utilisateur
        fields = ["id",
                  "nom",
                  "prenom",
                  "email",
                  "tel",
                  "statut",
                  "myMessages"
                  ]


class NewUtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ["id",
                  "nom",
                  "prenom",
                  "email",
                  "tel",
                  "statut",
                  ]
