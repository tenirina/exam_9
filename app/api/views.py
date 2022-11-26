from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import ImageSerializer

from webapp.models import Image


class FavoriteView(APIView):

    def create(self, request, *args, **kwargs):
        image = get_object_or_404(Image, pk=kwargs.get('pk'))
        user = request.user
        if not user.favorites.filter(users=user).exists():
            user.favorites.add(image)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        image = get_object_or_404(Image, pk=kwargs.get('pk'))
        user = request.user
        if user.favorites.filter(users=user):
            user.favorites.remove(image)
        return Response(status=status.HTTP_204_NO_CONTENT)
