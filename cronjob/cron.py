from datetime import datetime
from datetime import timedelta

from scheduler.models import Scheduler

def update_time():
  current_time = datetime.now()
  print(current_time)
  medications_due = Scheduler.objects.filter(
    next_dosage__day=current_time.day
    ).filter(
      next_dosage__hour=current_time.hour
    ).filter(
      next_dosage__minute=current_time.minute
    )
  for med_schedule in medications_due:
    med_schedule['last_dosage'] = med_schedule['next_dosage']
    med_schedule['next_dosage'] = med_schedule['next_dosage'] + timedelta(med_schedule['hours'])