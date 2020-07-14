from django.urls import path

from .views import MedicationList, MedicationDetail

urlpatterns = [
  path('', MedicationList.as_view(), name='medication_list'),
  path('<int:pk>/', MedicationDetail.as_view(), name='medication_detail')
]