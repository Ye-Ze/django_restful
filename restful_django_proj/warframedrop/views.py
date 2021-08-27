from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class MissionRewardViewSet(viewsets.ModelViewSet):
    queryset = MissionRewards.objects.all()
    serializer_class = MissionRewardsSerializer
