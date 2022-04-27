from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from StudentApp.models import Student
from StudentApp.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# ************************* Student view *********************************
@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        json_data = request.body
        print(json_data)
        stream_data = io.BytesIO(json_data)
        print(stream_data)
        python_data = JSONParser().parse(stream_data)
        print(python_data)
        id = python_data.get('id', None)
        print("The requested Id", id)
        if id is not None:
            stu = Student.objects.get(id=id)
            print("The query data set", stu)
            serializer = StudentSerializer(stu)
            print("The serialized data", serializer)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    # Taking json data from third party app and save in database
    if request.method == 'POST':
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()

            res = {'msg': 'Data received and saved to database'}
            json_res = JSONRenderer().render(res)
            return HttpResponse(json_res, content_type='application/json')
        json_res = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_res, content_type='application/json')

    # updating data in database using third party app
    if request.method == 'PUT':
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()

            res = {'msg': 'The requested details updated in the database'}
            json_res = JSONRenderer().render(res)
            return HttpResponse(json_res, content_type='application/json')
        json_res = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_res, content_type='application/json')

    # deletes requested data as per third party app request
    if request.method == 'DELETE':
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()

        res = { 'msg': 'The requested entry deleted from database'}
        json_res = JSONRenderer().render(res)
        return HttpResponse(json_res, content_type='application/json')
