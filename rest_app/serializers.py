from rest_framework import serializers
from .models import Employess

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employess
        fields = '__all__'
