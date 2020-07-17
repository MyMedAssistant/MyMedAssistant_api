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
      'dosage_count',
      'start',
      'last',
      'next_dosage',
      'end',
      'user_id_medication'
      )