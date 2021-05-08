from django.contrib import admin
from .models import Agency


class AgencyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "address",
        "email",
    )


admin.site.register(Agency, AgencyAdmin)
