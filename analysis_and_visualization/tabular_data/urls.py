from django.urls import path
from . import views

urlpatterns = [
    path('tables/', views.getUploadedTables, name='tables'),
    path('tables/create/', views.createUploadedTable, name='createTable'),

]