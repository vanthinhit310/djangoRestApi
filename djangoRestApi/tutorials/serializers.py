from rest_framework import serializers
from tutorials.models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # Once the request data has been validated, we can create a todo item instance in the database
        return Tutorial.objects.create(
            title=validated_data.get("title"),
            description=validated_data.get("description"),
        )

    def update(self, instance, validated_data):
        # Once the request data has been validated, we can update the todo item instance in the database
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance

    class Meta:
        model = Tutorial
        fields = "__all__"
