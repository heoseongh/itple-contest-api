from rest_framework import serializers, viewsets
from .models import Contest


class ContestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contest
        fields ='__all__'

        # fields = [
        #     'id',
        #     'title',
        #     'image_url',
        #     'tags',
        #     'summary',
        #     'detail',
        #     'created_at',
        #     'updated_at'
        # ]
