from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.getUploadedTables, name='templates'),
    path('templates/create/', views.createUploadedTable, name='createTable'),
    path('templates/visualize/<str:table_id>', views.render_csv_table, name="renderTable"),
    path('templates/delete/<str:id>', views.deleteUploadedTable, name="deleteTable")

]