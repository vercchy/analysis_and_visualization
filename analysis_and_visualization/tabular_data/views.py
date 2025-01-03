from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated

from .models import UploadedTable
from .serializers import UploadedTableSerializer, CreateUploadedTableSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwnerOfTable


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUploadedTables(request):
    user = request.user
    tables = UploadedTable.objects.filter(user=user)
    serializer = UploadedTableSerializer(tables, many=True)
    return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def createUploadedTable(request):
    serializer = CreateUploadedTableSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save(user=request.user)

        uploaded_file = request.data.get('csv_file')
        if uploaded_file:
            instance.save_csv_content(uploaded_file)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUploadedTable(request, id):
    table = get_object_or_404(UploadedTable, pk=id, user=request.user)
    table.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def render_csv_table(request, table_id):
    table = get_object_or_404(UploadedTable, pk=table_id)
    if table:
        html_table = table.generate_visual_representation()
        return Response(html_table, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
