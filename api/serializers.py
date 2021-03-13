from rest_framework import serializers
from .models import *


class GiveawaySerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField()

    def get_participants(self, obj):
        queryset = obj.participants.all()
        serializer = ParticipantSerializer(queryset, many=True)
        return serializer.data

    class Meta:
        model = Giveaway
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
