from django.urls import path

from webapp.views.base import IndexView
from webapp.views.images import CreateImageView, ImageView, DeleteImageView, UpdateImageView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateImageView.as_view(), name='image_create'),
    path('detail/<int:pk>', ImageView.as_view(), name='image'),
    path('update/<int:pk>', UpdateImageView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteImageView.as_view(), name='delete'),
    path('confirm-delete/<int:pk>', DeleteImageView.as_view(), name='confirm_delete'),
]
