from django.urls import path

from .views import update_time

urlpatterns = [
  path('', update_time, name='update_time'),
]