from rest_framework import serializers
from .models import Advice

class AdviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advice
        fields = "__all__"