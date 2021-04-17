from rest_framework import serializers, viewsets
from .models import Contest

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contest
        fields = ['id','title','desc']  
        # fields ='__all__'