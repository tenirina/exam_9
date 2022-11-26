from django.contrib import admin

from webapp.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'text', 'author', 'created_at')
    list_filter = ('id', 'text', 'author')
    search_fields = ('id', 'text', )
    fields = ('id', 'image', 'text', 'author', 'favorites', 'created_at')
    readonly_fields = ('id', 'author')


admin.site.register(Image, ImageAdmin)
