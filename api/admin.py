from django.contrib import admin
from .models import *


class ParticipantInline(admin.TabularInline):
    model = Participant


class WinnerInline(admin.TabularInline):
    model = Winner


class GiveawayAdmin(admin.ModelAdmin):
    inlines = [WinnerInline, ParticipantInline]


admin.site.register(Giveaway, GiveawayAdmin)
admin.site.register(Participant)
admin.site.register(Winner)

admin.site.site_url = '/'
admin.site.index_title = 'Admin'
admin.site.site_title = 'Giveaway'
admin.site.site_header = 'Giveaway Administration'
