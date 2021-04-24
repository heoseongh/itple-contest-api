from rest_framework import serializers, viewsets
from .models import Contest


# fields ='__all__' * 모든 필드를 JSON 데이터에 포함시킨다.
# JSON 데이터에 담길 내용을 커스텀하려면 아래의 주석처럼 필드를 입맛에 맞게 선언해주면 된다.
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
