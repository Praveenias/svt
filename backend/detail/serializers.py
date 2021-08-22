from django.db.models import fields
from rest_framework import serializers

from .models import Details

class Detailserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Details
        fields = ('name','price','model')