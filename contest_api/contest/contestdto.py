from .models import Contest
from rest_framework import serializers

class ContestSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contest
        fields = ['name','desc','poster']