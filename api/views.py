from django.shortcuts import render, get_object_or_404
from .models import Utilisateur, Message
from .serializers import MessageSerializer, MessageUtilisateurSerializer, UtilisateurSerializer, NewUtilisateurSerializer
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


class UserRetrieveView(generics.RetrieveAPIView):
    serializer_class = UtilisateurSerializer
    queryset = Utilisateur.objects.all()


class UserListView(generics.ListAPIView):
    serializer_class = UtilisateurSerializer
    queryset = Utilisateur.objects.all()


class MedecinsListView(generics.ListAPIView):
    serializer_class = UtilisateurSerializer
    queryset = Utilisateur.objects.filter(statut='medecin')


class UserCreateView(generics.CreateAPIView):
    serializer_class = NewUtilisateurSerializer
    queryset = Utilisateur.objects.all()


class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # utilisateur = get_object_or_404(Utilisateur, email=email)
        try:
            utilisateur = Utilisateur.objects.get(email=email)
        except Utilisateur.DoesNotExist:
            return Response({"error": "Votre compte n'existe pas"}, status=status.HTTP_400_BAD_REQUEST)

        if utilisateur.password != password:
            return Response({"error": "entrez le vrai mot de passe"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(status=status.HTTP_200_OK)


class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class MessagesApiView(APIView):
    def post(self, request, *args, **kwargs):
        message = request.data.get("message")
        destinataire_nom = request.data.get("destinataire_nom")
        destinataire_prenom = request.data.get("destinataire_prenom")
        utilisateur_id = request.data.get("utilisateur_id")

        msg = Message.objects.create(contenu=message, destinataireId=Utilisateur.objects.get(
            nom=destinataire_nom, prenom=destinataire_prenom).id)
        Utilisateur.objects.get(id=utilisateur_id).myMessages.add(msg)

        return Response({"response": "enregistré"}, status=201)
