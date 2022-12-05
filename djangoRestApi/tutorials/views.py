from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from .models import Tutorial
from .serializers import TutorialSerializer

# Create your views here.
class TutorialView(APIView):
    def get(self, request, id=None):
        if id:
            # If an id is provided in the GET request, retrieve the tutorial item by that id
            try:
                # Check if the tutorial item the user wants to update exists
                queryset = Tutorial.objects.get(id=id)
            except Tutorial.DoesNotExist:
                # If the tutorial item does not exist, return an error response
                return Response(
                    {"errors": "This tutorial item does not exist."}, status=400
                )

            # Serialize tutorial item from Django queryset object to JSON formatted data
            read_serializer = TutorialSerializer(queryset)

        else:
            # Get all tutorial items from the database using Django's model ORM
            queryset = Tutorial.objects.all()

            # Serialize list of tutorials item from Django queryset object to JSON formatted data
            read_serializer = TutorialSerializer(queryset, many=True)

            # Return a HTTP response object with the list of tutorial items as JSON
            return Response(read_serializer.data)

    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer = TutorialSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():

            # If user data is valid, create a new tutorial item record in the database
            tutorial_item_object = create_serializer.save()

            # Serialize the new tutorial item from a Python object to JSON format
            read_serializer = TutorialSerializer(tutorial_item_object)

            # Return a HTTP response with the newly created tutorial item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)
