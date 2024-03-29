from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Post, Category


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'created', 'modified', 'published', 'sponsored']
    search_fields = ['title', 'content']
    list_filter = ['published', 'sponsored']
    filter_horizontal = ['tags']
    autocomplete_fields = ('tags',)
    resource_class = PostResource


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]
    pass
