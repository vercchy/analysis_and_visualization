from django.urls import path
from . import views

urlpatterns = [
    path('tables', views.UploadedTableListAPIView.as_view(), name='tables'),
    path('tables/<int:user_id>', views.UploadedTableByUserIdAPIView.as_view(), name='user-uploaded-tables'),
]