from rest_framework import serializers

# Import your model here
from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker  # this is the model that is being serialized
        fields = '__all__'

        # For partial serialization un-mark below line
        # fields = ('id', 'first_name')
