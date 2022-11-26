from django.urls import path

from api.views import FavoriteCreateView, FavoriteDeleteView

urlpatterns = [
    path('image/<int:pk>/favorite/', FavoriteCreateView.as_view(), name='favorites_create'),
    path('image/<int:pk>/not-favorite/', FavoriteDeleteView.as_view(), name='favorites_delete')
]
