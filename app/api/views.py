import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from webapp.models import Image


class FavoriteCreateView(APIView):

    def post(self, request, *args, **kwargs):
        image = get_object_or_404(Image, pk=kwargs.get('pk'))
        user = request.user
        if user.favorites.filter(users=user).exists():
            user.favorites.add(image)
        return Response(status=status.HTTP_200_OK)


class FavoriteDeleteView(APIView):

    def delete(self, request, *args, **kwargs):
        image = get_object_or_404(Image, pk=kwargs.get('pk'))
        user = request.user
        if user.favorites.filter(users=user):
            user.favorites.remove(image)
        return Response(status=status.HTTP_204_NO_CONTENT)
