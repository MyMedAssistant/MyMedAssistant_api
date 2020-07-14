from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Scheduler
from .serializers import SchedulerSerializer

# Create your views here.
class SchedulerList(ListCreateAPIView):
  queryset = Scheduler.objects.all()
  serializer_class = SchedulerSerializer

class SchedulerDetail(RetrieveUpdateDestroyAPIView):
  queryset = Scheduler.objects.all()
  serializer_class = SchedulerSerializer