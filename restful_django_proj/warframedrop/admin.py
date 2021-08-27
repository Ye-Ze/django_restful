from warframedrop.models import *
from django.contrib import admin


@admin.register(MissionRewards)
class MissionRewardsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rarity', 'chance',
                    'gameMode', 'isEvent', 'planet', 'mission', 'rotation']
    list_filter = ['rarity', 'gameMode', 'planet', 'rotation']
