from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class HelloView(APIView):
    def get(self, request):
        return Response("DJANGO REST API SERVICE!")
