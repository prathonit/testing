from django.shortcuts import render

from django.http import HttpResponse , JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employess
from .serializers import EmployeeSerializer
from rest_framework.decorators import  api_view

from rest_framework import serializers

#Create your views here.
class EmployessList(APIView):
    def get(self, request):
        emplyee1 = Employess.objects.all()
        serializer = EmployeeSerializer(emplyee1, many=True)
        return Response(serializer.data)
    def post(self):
        pass
# @api_view(['GET','POST'])
# def get_emp(request):
#     try:
#         emp = Employess.objects.all(pk = pk)
#     except Employess.DoesNotExist:
#         return HttpResponse(status = status.HTTP_400_BAD_REQUEST)
#     if request.method == "GET":
#         emp = Employess.objects.filter(first_name = "Prathmesh")
#         serializer = EmployeeSerializer(emp, many = True)
#         return Response(serializer.data)
#     # if request.method == "POST":
#     #     serializer = EmployeeSerializer(data = request.data)
#     #
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data)
#     #     else :
#     #         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         emp.delete()
#         return HttpResponse(status = status.HTTP_200_OK)
