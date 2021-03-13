from django.contrib import admin
from .models import *


admin.site.register(Giveaway)
admin.site.register(Participant)

admin.site.site_url = '/'
admin.site.index_title = 'Admin'
admin.site.site_title = 'Giveaway'
admin.site.site_header = 'Giveaway Administration'
