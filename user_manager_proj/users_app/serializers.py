from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # this is the model that is being serialized
        fields = '__all__'

        # For partial serialization un-mark below line
        # fields = ('id', 'first_name')
