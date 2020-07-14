from rest_framework import serializers

from .models import Medication

class MedicationSerializer(serializers.ModelSerializer):

  class Meta:
    model = Medication
    fields = ('id', 'medication_name', 'side_effects')