from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserList(ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer