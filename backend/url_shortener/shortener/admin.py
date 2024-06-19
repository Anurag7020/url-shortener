from django.contrib import admin
from .models import ShortenedURL, URLHit


# Register your models here.

class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ('user', 'original_url', 'short_code', 'created_at')
    search_fields = ('short_code', 'original_url')
    list_filter = ('created_at', 'user')


class URLHitAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_code', 'timestamp', 'ip_address')
    search_fields = ('short_code', 'ip_address')
    list_filter = ('timestamp', 'user')


admin.site.register(ShortenedURL, ShortenedURLAdmin)
admin.site.register(URLHit, URLHitAdmin)
