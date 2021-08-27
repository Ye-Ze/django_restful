from django.db.models import fields
from rest_framework import serializers
from .models import *


class MissionRewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionRewards
        fields = (
            "id",
            "name",
            "rarity",
            "chance",
            "gameMode",
            "isEvent",
            "planet",
            "mission",
            "rotation",
        )
