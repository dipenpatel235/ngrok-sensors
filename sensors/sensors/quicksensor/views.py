from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404

from rest_framework import viewsets
from rest_framework import status

from rest_framework.test import APIRequestFactory
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from sensors.quicksensor.serializers import SensorsSerializer
from sensors.quicksensor.serializers import GroupSerializer
from sensors.quicksensor.serializers import UserSerializer

from sensors.quicksensor.models import Sensors
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist


from django.http import HttpResponse
import json
from django.core import serializers


import logging
logger = logging.getLogger(__name__)

NGROK_TOKEN='5q2VZdxrGZYALSG5PZ7eB_A8DWf7eQZGwtw9KDyGoy'

factory = APIRequestFactory()
request = factory.get('/')

serializer_context = {
    'request': Request(request),
}

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SensorsViewSet(viewsets.ModelViewSet):

    allowed_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    serializer_class = SensorsSerializer
    queryset = Sensors.objects.all()

class AddSensorApiViewSet(APIView):
    def get(self,request):
        todo=Sensors.objects.all()
        serializer=SensorsSerializer(todo,many=True)
        return Response({'received data': 'AAA'})

    def post(self,request,format=None):
         serializer = SensorsSerializer(data=request.data,context=serializer_context)
         if serializer.is_valid():
             serializer.save()
             content={'token':serializer.data['sensorid'],'ngrokid':NGROK_TOKEN}
             return Response(content)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, *args, **kwargs):
        testmodel = Sensors.objects.get(sensorid=request.data['sensorid'])
        serializer = SensorsSerializer(testmodel, data=request.data, context=serializer_context) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            

class InstallSensorApiViewSet(APIView): 
    def get(self,request):        
        try:
            sensorid = Sensors.objects.get(sensorid=request.GET['sensorid'])
            dict_obj = model_to_dict( sensorid )
            if (request.GET['sensorid'] == dict_obj['sensorid'] and request.GET['ip'] == dict_obj['ip'] ):
                sensorid = dict_obj['sensorid']
                ip = dict_obj['ip']
                content={'sensorid':sensorid, 'ngrokid':NGROK_TOKEN}
                return Response(content)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)            
        except ObjectDoesNotExist:
            return Response(text="Please contact admin. requested details not match.", status=status.HTTP_400_BAD_REQUEST)            