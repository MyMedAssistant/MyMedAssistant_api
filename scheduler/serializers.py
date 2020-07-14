from rest_framework import serializers

from .models import Scheduler

class SchedulerSerializer(serializers.ModelSerializer):

  class Meta:
    model = Scheduler
    fields = (
      'id',
      'user',
      'medication',
      'hours',
      'dosage',
      'start',
      'next_dosage',
      'end',
      'user_id_medication'
      )