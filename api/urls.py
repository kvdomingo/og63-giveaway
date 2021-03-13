from django.urls import path
from .views import *

urlpatterns = [
    path('giveaway', GiveawayView.as_view()),
    path('participant', ParticipantView.as_view()),
]
