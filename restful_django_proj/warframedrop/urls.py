from django.urls import path, include

from warframedrop import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('drop', views.MissionRewardViewSet)

urlpatterns = [
    path('wf/', include(router.urls)),
]
