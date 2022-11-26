from django.views.generic import ListView

from webapp.models import Image


class IndexView(ListView):
    template_name = 'index.html'
    model = Image

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        images = Image.objects.all().order_by('-updated_at')
        context['images'] = images
        return context
