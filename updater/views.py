from rest_framework.generics import ListAPIView

from datetime import datetime
from datetime import timedelta

from scheduler.models import Scheduler
from scheduler.serializers import SchedulerSerializer

class UpdateTime(ListAPIView):
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
  queryset = Scheduler.objects.all()
  serializer_class = SchedulerSerializer