from django.contrib.auth import get_user_model
from django.db import models


class Image(models.Model):
    image = models.ImageField(verbose_name='Photo', null=False, blank=False, upload_to='images')
    text = models.CharField(verbose_name='Text', null=False, blank=False, max_length=100)
    author = models.ForeignKey(verbose_name='Author', to=get_user_model(), related_name='images', null=False, blank=False,
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date of change', auto_now=True)
    users = models.ManyToManyField(to=get_user_model(), related_name='favorites', blank=True)

    def __str__(self):
        return f'{self.author} : {self.text[:30]}'
