from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'writer',
        'email',
        'content',
    )


admin.site.register(Contact, ContactAdmin)