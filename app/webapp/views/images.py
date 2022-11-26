from django.views.generic import DetailView, CreateView
from django.urls import reverse

from webapp.forms import ImageForm
from webapp.models import Image


class CreateImageView(CreateView):
    template_name = 'images/create.html'
    form_class = ImageForm
    model = Image

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')

