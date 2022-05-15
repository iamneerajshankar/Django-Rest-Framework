from django.shortcuts import render
from rest_framework import viewsets
from api.models import Employee, ApiType
from api.serializers import EmployeeSerializer, ApiTypeSerializer
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets


def home_page(request):
    api_type_qs = ApiType.objects.all()
    return render(request, 'index.html', {'api_type': api_type_qs})


class ApiTypeModelViewSet(viewsets.ModelViewSet):
    queryset = ApiType.objects.all()
    serializer_class = ApiTypeSerializer


# using Model View Sets
class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# Generic View based API
class EmployeeCreateAndList(CreateModelMixin, ListModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeModification(RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# function based Rest Api
@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def function_based_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            emp_data = Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(emp_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        emp_data = Employee.objects.all()
        serializer = EmployeeSerializer(emp_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Response': 'Congratulations..!!! Data Received and saved.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    if request.method == 'PUT':
        emp_data = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(emp_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Response': 'Requested data updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        emp_data = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(emp_data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Response': 'Requested data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        emp_data = Employee.objects.get(id=pk)
        emp_data.delete()
        return Response({'Response': 'Requested data deleted'}, status=status.HTTP_202_ACCEPTED)


# View Set based Rest Api
class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        print("*********List***********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        emp_qs = Employee.objects.all()
        serializer = EmployeeSerializer(emp_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        id =pk
        if id is not None:
            emp_qs = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp_qs)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Response': 'The created in the database'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        emp_qs = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp_qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Response': 'The requested data updated in the database'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        emp_qs = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp_qs, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Response': 'The requested data updated in the database'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        emp_qs = Employee.objects.get(id=pk)
        emp_qs.delete()
        return Response({'Response': 'The requested data deleted'}, status=status.HTTP_204_NO_CONTENT)




