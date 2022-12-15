
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from notifications.models import Notification

from .serializers import NotificationSerializer


class NotificationListAPIView(ListAPIView):
    """
        Vizualizare care returnează lista de notificări a unui singur utilizator.
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Notification.get_user_notification(self.request.user)
        unread_notifications = queryset_list.filter(is_read=False)
        # Pentru ca acest flag să poată fi folosit în front-end în scopuri de stilizare.

        for notification in unread_notifications:
            notification.is_read = True
            notification.save()
        return queryset_list
