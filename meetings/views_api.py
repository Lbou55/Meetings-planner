from rest_framework import viewsets
from .models import Room, Meeting
from .serializers import RoomSerializer, MeetingSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.select_related('room')
    serializer_class = MeetingSerializer

