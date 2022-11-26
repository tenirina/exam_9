from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from webapp.models import Image


class IndexView(ListView):
    template_name = 'index.html'
    ordering = ('-created_at',)
    model = Image
