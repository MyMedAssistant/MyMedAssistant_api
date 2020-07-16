from datetime import datetime
from datetime import timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()


from scheduler.models import Scheduler

@sched.scheduled_job('cron', minute=*/1)
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

sched.start()

if __name__ == "__main__":
    update_time()