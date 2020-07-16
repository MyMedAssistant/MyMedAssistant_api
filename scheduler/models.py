from django.db import models

class Scheduler(models.Model):
  user = models.CharField(max_length=64)
  medication = models.CharField(max_length=64)
  hours = models.IntegerField()
  dosage = models.CharField(max_length=256)
  start = models.DateTimeField(auto_now=False, auto_now_add=False)
  last = models.DateTimeField(auto_now=False, auto_now_add=False)
  next_dosage = models.DateTimeField(auto_now=False, auto_now_add=False)
  end = models.DateTimeField(auto_now=False, auto_now_add=False)
  user_id_medication = models.CharField(max_length=64)

  def __str___(self):
    return self.user_id_medication


from datetime import datetime
from datetime import timedelta

def update_time():
  current_time = datetime.now()
  print('UPDATE_TIME', str(current_time))
  simulated_time = current_time.replace(day=25, hour=13, minute=53)
  medications_due = Scheduler.objects.filter(id=9)
  # medications_due = Scheduler.objects.filter(
  #     next_dosage__day=simulated_time.day
  #   ).filter(
  #     next_dosage__hour=simulated_time.hour
  #   ).filter(
  #     next_dosage__minute=simulated_time.minute
  #   )
  for med_schedule in medications_due:
    print(med_schedule)
    med_schedule.last = med_schedule.next_dosage
    med_schedule.next_dosage = med_schedule.next_dosage + timedelta(hours=med_schedule.hours)
    med_schedule.save()

if __name__ == "__main__":
  update_time()