from django.contrib.admin.widgets import AdminFileWidget
from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from .views import Photo


class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            t = get_thumbnail(value, "150")
            output.append(f'<a href="{value.url}" target="_blank"><img src="{t.url}"></a>')
        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return ''.join(output)


class PhotoInLine(admin.StackedInline):
    model = Photo
    fields = ['title', 'slug', 'short_description', 'image', 'status']
    readonly_fields = ['slug']
    extra = 1
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }
