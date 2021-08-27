from django.db import models
from uuid import uuid4


class MissionRewards(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    rarity = models.CharField(max_length=255)
    chance = models.FloatField()
    gameMode = models.CharField(max_length=255)
    isEvent = models.BooleanField()
    planet = models.CharField(max_length=255)
    mission = models.CharField(max_length=255)
    rotation = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def as_dict(self):
        json = {
            "id": str(self.id),
            "name": self.name,
            "rarity": self.rarity,
            "chance": self.chance,
            "gameMode": self.gameMode,
            "isEvent": self.isEvent,
            "planet": self.planet,
            "mission": self.mission,
            "rotation": self.rotation,
        }
        return json
