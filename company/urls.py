from django.urls import path
from .views import EmployeeDetails, EmployeeAPIView, GenericAPIView

urlpatterns = [
    path('employee/', EmployeeAPIView.as_view()),
    #  path('employee/', EmployeeAPIView.as_view()),
    path('detail/<int:pk>', EmployeeDetails.as_view()),
    path('generic/employee/<int:pk>', GenericAPIView.as_view()),

]
