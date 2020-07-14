from django.db import models

# Create your models here.

class Medication(models.Model):
  medication_name = models.CharField(max_length=64)
  side_effects = models.CharField(max_length=512)

  def __str__(self):
    return self.medication_name
