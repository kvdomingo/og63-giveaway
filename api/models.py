from django.utils import timezone
from django.db import models
from django.conf import settings


class Giveaway(models.Model):
    created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=256)
    prize = models.CharField(max_length=256)
    num_winners = models.PositiveIntegerField()
    eligibility = models.TextField()
    rules = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class Participant(models.Model):
    username = models.CharField(max_length=64)
    joined = models.DateTimeField(default=timezone.now)
    giveaway = models.ForeignKey(
        Giveaway,
        related_name='participants',
        related_query_name='giveaways',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ['username', 'giveaway']
        ordering = ['joined']

    def __str__(self):
        return self.username


class Winner(models.Model):
    participant = models.ForeignKey(Participant, related_name='giveaways_won', on_delete=models.CASCADE)
    giveaway = models.ForeignKey(Giveaway, related_name='winners', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['participant', 'giveaway']

    def __str__(self):
        return f'{self.giveaway.name} - {self.participant.username}'
