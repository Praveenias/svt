from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Detailserializers
from .models import Details
# Create your views here.

class Detailview(viewsets.ModelViewSet):
    queryset = Details.objects.all().order_by('name')
    serializer_class = Detailserializers

