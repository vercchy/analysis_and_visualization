from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import UploadedTable
from .serializers import UploadedTableSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwner


class UploadedTableListAPIView(generics.ListAPIView):
    queryset = UploadedTable.objects.all()
    serializer_class = UploadedTableSerializer


class UploadedTableByUserIdAPIView(generics.ListAPIView):
    serializer_class = UploadedTableSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return UploadedTable.objects.filter(user=user_id)


class UploadedTableDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            instance = UploadedTable.objects.get(pk=pk)
            serializer = UploadedTableSerializer(instance)
            return Response(serializer.data)
        except UploadedTable.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

