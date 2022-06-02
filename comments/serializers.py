from rest_framework import serializers

from comments.models import Comments
from users.serializers import UsersSerializer

class CommentsSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = ('id', 'timestamp', 'content', 'user')
        read_only_fields = ('id', 'ticket', 'timestamp')
