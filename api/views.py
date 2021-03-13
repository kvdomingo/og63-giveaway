from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class GiveawayView(APIView):
    def get(self, request):
        query = Giveaway.objects.first()
        serializer = GiveawaySerializer(query)
        return Response(serializer.data)


class ParticipantView(CreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
