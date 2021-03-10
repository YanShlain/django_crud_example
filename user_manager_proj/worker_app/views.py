from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Add model here
from .models import Worker

# Add serializers here
from .serializers import WorkerSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def worker(request):
    if request.method == 'GET':  # user requesting data

        snippets = Worker.objects.all()
        serializer = WorkerSerializer(snippets, many=True)

        return Response(serializer.data)

    if request.method == 'POST':  # user posting data
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
