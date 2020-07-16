from django.urls import path

from .views import UpdateTime

urlpatterns = [
  path('', UpdateTime.as_view(), name='update_time'),
]