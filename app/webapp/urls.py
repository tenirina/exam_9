from django.urls import path

from webapp.views.base import IndexView
from webapp.views.images import CreateImageView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateImageView.as_view(), name='image_create')
]
