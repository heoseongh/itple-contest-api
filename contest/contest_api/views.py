# status : 200_OK, 404_NOT_FOUND 과 같이 HTTP 상태를 제공하는 모듈
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .contestdto import ContestSerializer
from .models import Contest

# GET - 공모전 전체 조회
# POST - 공모전 생성


@api_view(['GET', 'POST'])
def contestList(request):
    if request.method == 'GET':
        contests = Contest.objects.all()
        serializer = ContestSerializer(contests, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


# GET - 공모전 단건 조회
# PUT - 공모전 수정
# DELETE - 공모전 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def contestDetail(request, pk):
    try:
        contest = Contest.objects.get(id=pk)
    except contest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContestSerializer(
            contest, many=False)  # 하나만 가져오기 때문에 many=False
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContestSerializer(contest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        contest.delete()
        return Response("공모전이 삭제되었습니다.")


# # GET - 공모전 세부 정보 조회
# # POST - 공모전 세부 정보 생성
# @api_view(['GET','POST'])
# def detailList(request):
#     if request.method == 'GET':
#         details = Detail.objects.all()
#         serializer = DetailSerializer(details,many=True)

#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = DetailSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data)
