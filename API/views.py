from rest_framework import viewsets
from .serializer import ProfesorSerializer
from .models import Profesor

# Create your views here.
class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
