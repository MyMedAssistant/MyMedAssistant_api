from django.urls import path

from .views import UpdateTime

urlpatterns = [
  path('', UpdateTime, name='update_time'),
]