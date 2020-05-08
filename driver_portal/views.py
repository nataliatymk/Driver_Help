from rest_framework import viewsets
from .serializers import AdviceSerializer
from .models import Advice

class AdviceView (viewsets.ModelViewSet):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer