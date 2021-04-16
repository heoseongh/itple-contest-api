from .models import Contest
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .contestdto import ContestSerializers


# Create your viewsets here.
"""
class ContestViewset(viewsets.ModelViewSet):
    queryset = Contest.object.all()
    serializer_class = ContestSerializers
"""

@api_view(['GET'])
def contestList(request):
    if request.method == 'GET':
        contests = Contest.objects.all()
        serializer = ContestSerializers(contests,many=True)
        return Response(serializer.data)
