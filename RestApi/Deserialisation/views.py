from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from Deserialisation.serializers import StudentDeSerialization
import io
from django.http import HttpResponse
# Create your views here.
@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        deserializer = StudentDeSerialization(data=python_data)
        if deserializer.is_valid():
            deserializer.save()
            res = {'msg': 'data received and created!!'}
            json_res = JSONRenderer().render(json_data)
            return HttpResponse(json_res, content_type='application/json')
        json_res = JSONRenderer().render(deserializer.errors)
        return HttpResponse(json_res, content_type='application/json')

