from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Add model here
from .models import Employee

# Add serializers here
from .serializers import EmployeeSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def country(request):
    if request.method == 'GET':  # user requesting data

        snippets = Employee.objects.all()
        serializer = EmployeeSerializer(snippets, many=True)

        return Response(serializer.data)

    if request.method == 'POST':  # user posting data
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
