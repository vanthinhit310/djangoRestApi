from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def index(request):
    return JsonResponse(
        {"success": True, "message": "success", "data": {"a": 10.56, "b": "Thinh"}},
        safe=False,
    )
