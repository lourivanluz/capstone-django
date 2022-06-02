from rest_framework import serializers


from tickets.models import Tickets, Projects


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = (
            "id",
            "title",
            "description",
        )
        read_only_fields = ("id",)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = (
            "id",
            "project",
            "author",
            "category",
            "description",
            "test_steps",
            "severity",
            "frequency",
            "status",
            "deadline",
        )
        read_only_fields = (
            "id",
            "author",
            "project",
        )


class TicketAddSerializer(serializers.ModelSerializer):
    # responsibles = serializers.ListField(child=serializers.UUIDField())
    # user_id = serializers.UUIDField()

    class Meta:
        model = Tickets
        fields = (
            "id",
            "project",
            "author",
            "category",
            "description",
            "test_steps",
            "severity",
            "frequency",
            "status",
            "deadline",
            "responsibles",
        )
        read_only_fields = (
            "id",
            "project",
            "author",
            "category",
            "description",
            "test_steps",
            "severity",
            "frequency",
            "status",
            "deadline",
        )
