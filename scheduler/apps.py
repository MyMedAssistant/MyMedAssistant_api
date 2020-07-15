from django.apps import AppConfig
import time
import schedule

from .update_schedule import update_time

class SchedulerConfig(AppConfig):
  name = 'scheduler'

  def ready(self):
    schedule.every().hour.at(':00').do(update_time)
    schedule.every().hour.at(':15').do(update_time)
    schedule.every().hour.at(':30').do(update_time)
    schedule.every().hour.at(':45').do(update_time)
    while True:
      schedule.run_pending()
      time.sleep(1)