from django.http import JsonResponse
from .models import UploadedTable
from django.forms.models import model_to_dict


def api_home(request, *args, **kwargs):
    model_data = UploadedTable.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
        return JsonResponse(data)
