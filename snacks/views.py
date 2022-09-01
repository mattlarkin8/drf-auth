from .models import Snack
from .serializers import SnackSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

class SnackList(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class SnackDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer