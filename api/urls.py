from django.urls import path
from .views import *

urlpatterns = [
    path('giveaway', GiveawayView.as_view()),
    path('participant', ParticipantView.as_view()),
    path('winner', WinnerView.as_view()),
    path('draw', DrawView.as_view()),
    path('publish', PublishWinnersView.as_view()),
]
