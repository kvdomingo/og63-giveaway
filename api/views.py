import random
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

random = random.SystemRandom()


class GiveawayView(APIView):
    def get(self, request):
        query = Giveaway.objects.first()
        serializer = GiveawaySerializer(query)
        return Response(serializer.data)


class ParticipantView(CreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class WinnerView(APIView):
    def get(self, request):
        queryset = Giveaway.objects.first().winners.all()
        serializer = WinnerSerializer(queryset, many=True)
        return Response(serializer.data)


class DrawView(APIView):
    def post(self, request):
        data = request.data
        if data['token'] != settings.DRAW_TOKEN:
            return Response(dict(error='Invalid token'), status=status.HTTP_403_FORBIDDEN)
        queryset = Giveaway.objects.first().participants.all()
        serializer = ParticipantSerializer(queryset, many=True)
        response = dict(
            isValidToken=True,
            participantsList=serializer.data,
        )
        return Response(response, status=status.HTTP_200_OK)


class PublishWinnersView(CreateAPIView):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(PublishWinnersView, self).get_serializer(*args, **kwargs)
