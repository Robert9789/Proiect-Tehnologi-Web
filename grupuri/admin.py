
from django.contrib import admin

from .models import Board


class BoardAdmin(admin.ModelAdmin):
    """
    Admin settings for grups.
    """
    list_display = ('title', 'created', 'updated')
    date_hierarchy = 'created'


admin.site.register(Board, BoardAdmin)  # noqa: E305
