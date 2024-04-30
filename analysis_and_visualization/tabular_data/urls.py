from django.urls import path
from . import views

urlpatterns = [
    path('tables', views.getUploadedTables, name='tables'),
    path('tables/detail/<int:pk>', views.UploadedTableDetailAPIView.as_view(), name='tables-detail'),
]