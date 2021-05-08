from django.contrib import admin
from .models import Agent


class AgentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "agency",
        "phone",
        "email",
        "date_joined",
    )
    list_display_links = (
        "id",
        "name",
    )
    list_filter = (
        "date_joined",
        "agency",
    )
    search_fields = ("name",)


admin.site.register(Agent, AgentAdmin)
