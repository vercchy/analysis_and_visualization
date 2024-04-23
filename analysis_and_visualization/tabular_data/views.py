from django.http import JsonResponse
from .models import UploadedTable


def api_home(request, *args, **kwargs):
    model_data = UploadedTable.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['user_email'] = model_data.user.email
        data['user_first_name'] = model_data.user.first_name
        data['user_last_name'] = model_data.user.last_name
        data['csv_content'] = model_data.csv_content
        data['uploaded_at'] = model_data.uploaded_at
        return JsonResponse(data)
