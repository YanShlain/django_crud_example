from rest_framework import serializers

# Import your model here
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee  # this is the model that is being serialized
        fields = '__all__'

        # For partial serialization un-mark below line
        # fields = ('id', 'first_name')
