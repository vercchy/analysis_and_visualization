from rest_framework import generics
from .models import UploadedTable
from .serializers import UploadedTableSerializer


class UploadedTableListAPIView(generics.ListAPIView):
    queryset = UploadedTable.objects.all()
    serializer_class = UploadedTableSerializer


class UploadedTableByUserIdAPIView(generics.ListAPIView):
    serializer_class = UploadedTableSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return UploadedTable.objects.filter(user=user_id)
