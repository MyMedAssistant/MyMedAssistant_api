from datetime import datetime
from datetime import timedelta
from django.http import HttpResponse

from scheduler.models import Scheduler

def update_time(request):
  current_time = datetime.now()
  medications_due = Scheduler.objects.filter(
      next_dosage__day=current_time.day
    ).filter(
      next_dosage__hour=current_time.hour
    ).filter(
      next_dosage__minute=current_time.minute
    )
  for med_schedule in medications_due:
    med_schedule.last = med_schedule.next_dosage
    med_schedule.next_dosage = med_schedule.next_dosage + timedelta(hours=med_schedule.hours)
    med_schedule.dosage_count = med_schedule.dosage_count - 1
    med_schedule.save()
  return HttpResponse("I'm happy")
