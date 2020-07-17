from django.db import models

class Scheduler(models.Model):
  user = models.CharField(max_length=64)
  medication = models.CharField(max_length=64)
  hours = models.IntegerField()
  dosage = models.CharField(max_length=256)
  dosage_count = models.IntegerField()
  start = models.DateTimeField(auto_now=False, auto_now_add=False)
  last = models.DateTimeField(auto_now=False, auto_now_add=False)
  next_dosage = models.DateTimeField(auto_now=False, auto_now_add=False)
  end = models.DateTimeField(auto_now=False, auto_now_add=False)
  user_id_medication = models.CharField(max_length=64)

  def __str___(self):
    return self.user_id_medication