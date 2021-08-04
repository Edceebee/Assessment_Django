from rest_framework import serializers


# Serializers define the API representation.
class AnswerSerializer(serializers.Serializer):
    distance = serializers.CharField()

