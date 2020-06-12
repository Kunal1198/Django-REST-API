from django.http import JsonResponse
from django.shortcuts import render

# third party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import StudentSerializer
from .models import Student


class TestView(APIView):


    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        post = qs.first()
        serializer = StudentSerializer(qs, many=True)
        #serializer = StudentSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)