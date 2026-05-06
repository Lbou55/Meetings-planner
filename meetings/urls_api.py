from rest_framework.routers import DefaultRouter
from .views_api import RoomViewSet,MeetingViewSet

router=DefaultRouter()
router.register(r'rooms',RoomViewSet)
router.register(r'meetings',MeetingViewSet)

urlpatterns=router.urls