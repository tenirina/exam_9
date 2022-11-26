from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet

from webapp.forms import ImageForm
from webapp.models import Image


class CreateImageView(LoginRequiredMixin, CreateView):
    template_name = 'images/create.html'
    form_class = ImageForm
    model = Image

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class ImageView(DetailView):
    template_name = "images/image.html"
    model = Image
    fields = ('image', 'description',)


class UpdateImageView(LoginRequiredMixin, UpdateView):
    template_name = 'images/update.html'
    form_class = ImageForm
    model = Image
    context_object_name = 'image'

    def post(self, request, *args, **kwargs):
        img = Image.objects.get(pk=kwargs['pk'])
        if request.user == img.author or request.user.has_perm('webapp.change_image'):
            return super().post(request, *args, **kwargs)
        else:
            return reverse('index')

    def get_success_url(self):
        return reverse('image', kwargs={'pk': self.object.pk})


class DeleteImageView(LoginRequiredMixin, DeleteView):
    template_name = 'images/delete.html'
    model = Image
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        img = Image.objects.get(pk=kwargs['pk'])
        if request.user == img.author or request.user.has_perm('webapp.delete_image'):
            return super().post(request, *args, **kwargs)
        else:
            return reverse('index')



