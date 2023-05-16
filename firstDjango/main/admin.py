from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


# admin.site.site_header = "My panel administration DURAJ"
# admin.site.site_title = "DURAJ ADMIN Portal"
