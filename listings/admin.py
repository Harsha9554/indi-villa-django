from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "is_published",
        "price",
        "list_date",
        "city",
        "state",
    )
    list_display_links = (
        "id",
        "title",
    )
    list_filter = (
        "agent",
        "city",
        "list_date",
    )
    list_editable = ("is_published",)
    search_fields = (
        "title",
        "address",
        "city",
        "state",
    )


admin.site.register(Listing, ListingAdmin)
