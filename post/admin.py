from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'writer',
        'title',
        'registered_date',
    )
    search_fields = ('writer', 'title')


admin.site.register(Post, PostAdmin)
