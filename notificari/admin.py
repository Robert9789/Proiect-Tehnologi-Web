
from django.contrib import admin

from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    """
    Admin setari pt notificari.
    """
    list_display = ('notif_type', 'Actor', 'Object', 'Target', 'is_read', 'created')
    list_filter = ('is_read', )
    date_hierarchy = 'created'


admin.site.register(Notification, NotificationAdmin)  # noqa: E305
