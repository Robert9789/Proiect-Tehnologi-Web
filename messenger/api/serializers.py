
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags.humanize import naturaltime

from rest_framework import serializers

from messenger.models import Message
from users.api.serializers import UserDetailSerializer


class ContactsListSerializer(serializers.ModelSerializer):
    """
    Serializer are reprezintă lista de contacte a unui utilizator.
    """

    screen_name = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'screen_name',
            'profile_picture',
        ]

    def get_screen_name(self, obj):
        """
        Returneaza user screen name.

        :return: string
        """
        return obj.profile.screen_name()

    def get_profile_picture(self, obj):
        """
        Returneaza user's profile picture link.

        :return: string
        """
        request = self.context.get('request')
        profile_picture_url = obj.profile.get_picture()
        return request.build_absolute_uri(profile_picture_url)


class MessageListSerializer(serializers.ModelSerializer):
    """
    Serializer are reprezintă mesaje.
    """

    from_user = ContactsListSerializer(read_only=True)
    data_naturaltime = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = [
            'id',
            'from_user',
            'message',
            'date',
            'data_naturaltime',
        ]

    def get_data_naturaltime(self, obj):
        """
        Returns readable time.

        :return: string
        """
        return naturaltime(obj.date)
