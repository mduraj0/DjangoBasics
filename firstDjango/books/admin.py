from datetime import datetime
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from .models import Book, Author


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


class YearListFilter(admin.SimpleListFilter):
    title = _('publication year')
    parameter_name = 'year'

    def lookups(self, request, model_admin):
        return (
            ('1995-2000', _('1995-2000')),
            ('2000-2005', _('2000-2005')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1995-2000':
            return queryset.filter(Q(publication_year__gte=1995) & Q(publication_year__lte=2000))
        if self.value() == '2000-2005':
            return queryset.filter(Q(publication_year__gte=2000) & Q(publication_year__lte=2005))


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ['title', 'publication_year', 'available']
    search_fields = ['title', 'description']
    list_filter = ['publication_year', 'available', YearListFilter]
    resource_class = BookResource


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass