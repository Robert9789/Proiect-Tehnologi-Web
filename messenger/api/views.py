
from django.contrib.auth.models import User

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from messenger.models import Message

from .serializers import ContactsListSerializer, MessageListSerializer


class ContactsListAPIView(ListAPIView):
    """
    View care returnează lista de contacte a utilizatorului
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ContactsListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = self.request.user.profile.contact_list.all().filter(is_active=True)
        return queryset_list


class MessageListAPIView(ListAPIView):
    """
    View care returnează coversația între doi utilizatori.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = MessageListSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.request.GET.get('username', '')
        queryset_list = Message.objects.filter(user=self.request.user, conversation__username=username)
        queryset_list.update(is_read=True)
        return queryset_list


class MessageCreateAPIView(APIView):
    """
    View care se ocupă de crearea mesajelor.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        to_user_username = data.get('to')
        message = data.get('message')

        from_user = self.request.user
        to_user = User.objects.filter(username=to_user_username)
        if to_user.count() == 1:
            if from_user != to_user:
                chat_msg = Message.send_message(from_user, to_user, message)
            # Return data serialized folosind new MessageSerializer
            return Response({"to": to_user, "message": message})
        return Response({"detail": "User does not exists."}, status=401)
