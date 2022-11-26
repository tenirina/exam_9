from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from webapp.models import Image


class IndexView(ListView):
    template_name = 'index.html'
    ordering = ('-created_at',)
    model = Image

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        images = Image.objects.all()
        context['images'] = images
        return context
