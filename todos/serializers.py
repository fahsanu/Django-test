# todos/serializers.py
from rest_framework import serializers
from .models import Todo, Schedule

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Todo

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'event_id',
            'event_name',
            'start_time',
            'end_time',
            'transportation_mode',
            'extra_prep_time',
            'note',
        )
        model = Schedule