from django.urls import path

from .views import SchedulerList, SchedulerDetail

urlpatterns = [
  path('', SchedulerList.as_view(), name='scheduler_list'),
  path('<int:pk>/', SchedulerDetail.as_view(), name='scheduler_detail')
]