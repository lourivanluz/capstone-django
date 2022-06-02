from rest_framework import serializers


from tickets.models import Tickets


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
    # assigned = serializers.ListField(child=serializers.UUIDField())
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
            "assigned",
        )

        extra_kwargs = {
            "id": {"required": False},
            "project": {"required": False},
            "author": {"required": False},
            "category": {"required": False},
            "description": {"required": False},
            "test_steps": {"required": False},
            "severity": {"required": False},
            "frequency": {"required": False},
            "status": {"required": False},
            "deadline": {"required": False},
        }


class TicketPatchSerializer(TicketAddSerializer):
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
            "assigned",
        )

        extra_kwargs = {
            "id": {"required": False},
            "project": {"required": False},
            "author": {"required": False},
            "category": {"required": False},
            "description": {"required": False},
            "test_steps": {"required": False},
            "severity": {"required": False},
            "frequency": {"required": False},
            "status": {"required": False},
            "deadline": {"required": False},
            "assigned": {"required": False},
        }
