from rest_framework import viewsets

from ..models import Promise
from .serializers import PromiseSerializer


class PromiseViewSet(viewsets.ModelViewSet):
    queryset = Promise.objects.all().order_by('-dt_promised')
    serializer_class = PromiseSerializer
