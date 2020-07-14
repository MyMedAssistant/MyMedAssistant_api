from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from .models import Medication
from .serializers import MedicationSerializer

# Create your views here.
class MedicationList(ListCreateAPIView):
  queryset = Medication.objects.all()
  serializer_class = MedicationSerializer

class MedicationDetail(RetrieveAPIView):
  queryset = Medication.objects.all()
  serializer_class = MedicationSerializer