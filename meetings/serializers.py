from rest_framework import serializers
from .models import Room,Meeting

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class MeetingSerializer(serializers.ModelSerializer):
    room=RoomSerializer(read_only=True)
    room_id=serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(),source='room',write_only=True)
    class Meta:
        model = Meeting
        fields = [
            'id',
            'title',
            'description',
            'start_time',
            'end_time',
            'room',
            'room_id',
        ]