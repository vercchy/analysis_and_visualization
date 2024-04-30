from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import UploadedTable
from .serializers import UploadedTableSerializer
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


class UploadedTableDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            instance = UploadedTable.objects.get(pk=pk)
            serializer = UploadedTableSerializer(instance)
            return Response(serializer.data)
        except UploadedTable.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
