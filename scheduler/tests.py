from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Scheduler
from datetime import datetime
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    ENVIRONMENT=(str, 'PRODUCTION')
)

# Create your tests here.
class SchedulerTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    testuser = get_user_model().objects.create_user(username=env.str('DB_USER'), password=env.str('DB_PASSWORD'))
    testuser.save()

    test_scheduler_data = Scheduler.objects.create(
      user = 'Johnny B Meds',
      medication = 'Ice Cream',
      hours = 1,
      dosage = '1 bowl',
      start = datetime(2020, 7, 16, 16, 20, 00),
      last = datetime(2020, 7, 16, 16, 20, 00),
      next_dosage = datetime(2020, 7, 16, 17, 20, 00),
      end = datetime(2200, 7, 16, 17, 20, 00),
      user_id_medication = 'Johnny - Ice Cream'
    )
  
  def test_scheduler_content(self):
    schedule = Scheduler.objects.get(id=1)
    actual_user = str(schedule.user)
    actual_medication = str(schedule.medication)
    actual_hours = str(schedule.hours)
    actual_dosage = str(schedule.dosage)
    actual_start = str(schedule.start)
    actual_last = str(schedule.last)
    actual_next_dosage = str(schedule.next_dosage)
    actual_end = str(schedule.end)
    actual_user_id_medication = str(schedule.user_id_medication)
    self.assertEqual(actual_user, 'Johnny B Meds')
    self.assertEqual(actual_medication, 'Ice Cream')
    self.assertEqual(actual_hours, '1')
    self.assertEqual(actual_dosage, '1 bowl')
    self.assertEqual(actual_start, '2020-07-16 16:20:00+00:00')
    self.assertEqual(actual_last, '2020-07-16 16:20:00+00:00')
    self.assertEqual(actual_next_dosage, '2020-07-16 17:20:00+00:00')
    self.assertEqual(actual_end, '2200-07-16 17:20:00+00:00')
    self.assertEqual(actual_user_id_medication, 'Johnny - Ice Cream')