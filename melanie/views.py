from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MoleSerializer
import os

from .classifier import classify
# Create your views here.
class UploadMole(CreateAPIView):
	serializer_class = MoleSerializer
	def post(self, request, format=None):
		serializer = MoleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			image_location = serializer.data['image']
			response = classify(image_location)
			os.remove(image_location)
			print(response, type(response))
			return JsonResponse(response)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)