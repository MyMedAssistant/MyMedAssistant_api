from django.apps import AppConfig
# import django
import time
import schedule

from .update_schedule import update_time
# django.setup()
def job():
  print('hi')

class SchedulerConfig(AppConfig):
  name = 'scheduler'

  def ready(self):
    schedule.every().hour.at(':00').do(job)
    schedule.every().hour.at(':15').do(job)
    schedule.every().hour.at(':30').do(job)
    schedule.every().hour.at(':45').do(job)
    # while True:
    #   schedule.run_pending()
    #   time.sleep(1)