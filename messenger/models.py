
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max


class Message(models.Model):
    """
    Model ce reprezinta mesajul
    """
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    message = models.TextField(max_length=1000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ('date', )
        db_table = 'messages_message'

    def __str__(self):
        """Unicode reprezentare pt message model."""
        return self.message

    @staticmethod
    def send_message(from_user, to_user, message):
        """
        Se ocupă de crearea mesajului.
        Creează două instanțe de mesaj care diferă cu doar trei câmpuri.
            :user
            :conversation
            :is_read
        """
        message = message[:1000]
        current_user_message = Message(from_user=from_user,
                                       message=message,
                                       user=from_user,
                                       conversation=to_user,
                                       is_read=True)
        current_user_message.save()
        Message(from_user=from_user, message=message, user=to_user, conversation=from_user).save()

        return current_user_message

    @staticmethod
    def get_conversations(user):
        """
        Returneaza  o list de users avand conversati cu  `user` ntroduși.
        """
        conversations = Message.objects.filter(user=user).values('conversation').annotate(
            last=Max('date')).order_by('-last')
        users = []
        for conversation in conversations:
            users.append({
                'user':
                User.objects.get(pk=conversation['conversation']),
                'last':
                conversation['last'],
                'unread':
                Message.objects.filter(user=user, conversation__pk=conversation['conversation'],
                                       is_read=False).count(),
            })

        return users
