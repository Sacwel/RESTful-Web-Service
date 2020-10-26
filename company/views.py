from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee
from .serializers import EmployeeSerializer


# Generic based view - the best one - less code, clearer
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def post(self, request, pk):
        return self.create(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# Class based view - better, because it allows to compose bits of reusable behaviour
class EmployeeAPIView(APIView):

    @staticmethod
    def get(request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Function based view
# @api_view(['GET', 'POST'])
# def employee_list(request):
#
#     if request.method == 'GET':
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = EmployeeSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetails(APIView):

    @staticmethod
    def get_object(request, pk):
        try:
            return Employee.objects.get(pk=pk)

        except Employee.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PUT', 'DELETE'])
# def employee_detail(request, pk):
#     try:
#         employee = Employee.objects.get(pk=pk)
#
#     except Employee.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = EmployeeSerializer(employee, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         employee.delete()
#         return HttpResponse(status=204)

# def home(request):
#     return render(request, 'index.html')


# Create your views here.


# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
