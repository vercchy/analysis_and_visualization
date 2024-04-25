from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json


# Create your views here.


@csrf_exempt
def register(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        email = json_data.get('email')
        first_name = json_data.get('first_name')
        last_name = json_data.get('last_name')
        password = json_data.get('password')
        date_of_birth = json_data.get('date_of_birth')

        if not (email and first_name and last_name and password and date_of_birth):
            return JsonResponse({"error": "All fields are required."}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"errror": "User with this email already exists"}, status=400)

        user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name,
                                        date_of_birth=date_of_birth)
        return JsonResponse({"message": "User registered successfully"}, status=201)
