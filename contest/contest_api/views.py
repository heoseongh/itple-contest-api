from rest_framework.decorators import api_view
from rest_framework.response import Response
from .contestdto import MemberSerializer
from .models import Contest

# Create your views here.
@api_view(['GET'])
def contestList(request):
    contests = Contest.objects.all()
    serializer = MemberSerializer(contests,many=True)
    return Response(serializer.data)