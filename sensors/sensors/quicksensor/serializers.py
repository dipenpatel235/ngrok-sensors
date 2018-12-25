from django.contrib.auth.models import User, Group
from rest_framework import serializers
from sensors.quicksensor.models import Sensors


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SensorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensors
        fields = '__all__'

# class AddSensorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AddSensor
#         fields = ("id", 'title','text', 'completed', 'created_at')