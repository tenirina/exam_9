from django.urls import path

from api.views import FavoriteView

urlpatterns = [
    path('projects/', FavoriteView.as_view(), name='favorites'),
]
