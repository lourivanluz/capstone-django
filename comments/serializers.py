from rest_framework import serializers

from comments.models import Comments
from users.serializers import UsersSerializer

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'ticket', 'timestamp', 'content')
        read_only_fields = ('id', 'ticket', 'timestamp')
