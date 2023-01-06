from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Restorans
from .serializer import Restoran_Seria
class Restorans_APP(viewsets.ModelViewSet):
    queryset = Restorans.objects.all() #берёт все данные
    serializer_class = Restoran_Seria
# Create your views here.
