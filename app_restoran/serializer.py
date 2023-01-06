from rest_framework import serializers,validators
from django.contrib.auth.models import User
from .models import Restorans
class Restoran_Seria(serializers.ModelSerializer):
    class Meta:
        model = Restorans
        fields = '__all__'