from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import *
from main.serializers import *


"""  Star CRUD model  """
# Employee model
# read
class GetAllEmployeeItems(ListAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializers


# create
class CreateAllEmployeeItems(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


#  update
class UpdateAllEmployeeItems(UpdateAPIView):
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializers


#  delete
class DeleteAllEmployeeItems(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers




# Patient model
# read
class GetAllPatientItems(ListAPIView):
    queryset = Patient.objects.all().order_by('-id')
    serializer_class = PatientSerializers


# create
class CreateAllPatientItems(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers


#  update
class UpdateAllPatientItems(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers


#  delete
class DeleteAllPatientItems(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers




# Room model
# read
class GetAllRoomItems(ListAPIView):
    queryset = Room.objects.all().order_by('-id')
    serializer_class = RoomSerializers


# create
class CreateAllRoomItems(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


#  update
class UpdateAllRoomItems(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


#  delete
class DeleteAllRoomItems(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers




# Payment model
# read
class GetAllPaymentItems(ListAPIView):
    queryset = Payment.objects.all().order_by('-id')
    serializer_class = PaymentSerializers


# create
class CreateAllPaymentItems(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializers_class = PaymentSerializers


#  update
class UpdateAllPaymentItems(UpdateAPIView):
    queryset = Payment.objects.all()
    serializers_class = PaymentSerializers


#  delete
class DeleteAllPaymentItems(DestroyAPIView):
    queryset = Payment.objects.all()
    serializers_class = PaymentSerializers




# Comment model
# read
class GetAllCommentItems(ListAPIView):
    queryset = Comment.objects.all().order_by('-id')
    serializers_class = CommentSerializers


# create
class CreateAllCommentItems(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializers_class = CommentSerializers


#  update
class UpdateAllCommentItems(UpdateAPIView):
    queryset = Comment.objects.all()
    serializers_class = CommentSerializers


#  delete
class DeleteAllCommentItems(DestroyAPIView):
    queryset = Comment.objects.all()
    serializers_class = CommentSerializers




# Income model
# read
class GetAllIncomeItems(ListAPIView):
    queryset = Income.objects.all().order_by('-id')
    serializers_class = IncomeSerializers


# create
class CreateAllIncomeItems(ListCreateAPIView):
    queryset = Income.objects.all()
    serializers_class = IncomeSerializers


#  update
class UpdateAllIncomeItems(UpdateAPIView):
    queryset = Income.objects.all()
    serializers_class = IncomeSerializers


#  delete
class DeleteAllIncomeItems(DestroyAPIView):
    queryset = Income.objects.all()
    serializers_class = IncomeSerializers




# Ravenue model
# read
class GetAllRavenueItems(ListAPIView):
    queryset = Ravenue.objects.all().order_by('-id')
    serializers_class = RavenueSerializers


# create
class CreateAllRavenueItems(ListCreateAPIView):
    queryset = Ravenue.objects.all()
    serializers_class = RavenueSerializers


#  update
class UpdateAllRavenueItems(UpdateAPIView):
    queryset = Ravenue.objects.all()
    serializers_class = RavenueSerializers


#  delete
class DeleteAllRavenueItems(DestroyAPIView):
    queryset = Ravenue.objects.all()
    serializers_class = RavenueSerializers




# Cassa model
# read
class GetAllCassaItems(ListAPIView):
    queryset = Cassa.objects.all().order_by('-id')
    serializers_class = CassaSerializers


# create
class CreateAllCassaItems(ListCreateAPIView):
    queryset = Cassa.objects.all()
    serializers_class = CassaSerializers


#  update
class UpdateAllCassaItems(UpdateAPIView):
    queryset = Cassa.objects.all()
    serializers_class = CassaSerializers


#  delete
class DeleteAllCassaItems(DestroyAPIView):
    queryset = Cassa.objects.all()
    serializers_class = CassaSerializers




# Operation model
# read
class GetAllOperationItems(ListAPIView):
    queryset = Operation.objects.all().order_by('-id')
    serializers_class = OperationSerializers


# create
class CreateAllOperationItems(ListCreateAPIView):
    queryset = Operation.objects.all()
    serializers_class = OperationSerializers


#  update
class UpdateAllOperationItems(UpdateAPIView):
    queryset = Operation.objects.all()
    serializers_class = OperationSerializers


#  delete
class DeleteAllOperationItems(DestroyAPIView):
    queryset = Operation.objects.all()
    serializers_class = OperationSerializers




# Department model
# read
class GetAllDepartmentItems(ListAPIView):
    queryset = Department.objects.all().order_by('-id')
    serializers_class = DepartmentSerializers


# create
class CreateAllDepartmentItems(ListCreateAPIView):
    queryset = Department.objects.all()
    serializers_class = DepartmentSerializers


#  update
class UpdateAllDepartmentItems(UpdateAPIView):
    queryset = Department.objects.all()
    serializers_class = DepartmentSerializers


#  delete
class DeleteAllDepartmentItems(DestroyAPIView):
    queryset = Department.objects.all()
    serializers_class = DepartmentSerializers




# Equipment model
# read
class GetAllEquipmentItems(ListAPIView):
    queryset = Equipment.objects.all().order_by('-id')
    serializers_class = EquipmentSerializers


# create
class CreaetAllEquipmentItems(ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializers_class = EquipmentSerializers


#  update
class UpdateAllEquipmentItems(UpdateAPIView):
    queryset = Equipment.objects.all()
    serializers_class = EquipmentSerializers


#  delete
class DeleteAllEquipmentItems(DestroyAPIView):
    queryset = Equipment.objects.all()
    serializers_class = EquipmentSerializers




# Info_about_cilinc model
# read
class GetAllInfo_about_cilincItems(ListAPIView):
    queryset = Info_about_cilinc.objects.all().order_by('-id')
    serializers_class = Info_about_cilincSerializers


# create
class CreateAllInfo_about_cilincItems(ListCreateAPIView):
    queryset = Info_about_cilinc.objects.all()
    serializers_class = Info_about_cilincSerializers


#  update
class UpdateAllInfo_about_cilincItems(UpdateAPIView):
    queryset = Info_about_cilinc.objects.all()
    serializers_class = Info_about_cilincSerializers


#  delete
class DeleteAllInfo_about_cilincItems(DestroyAPIView):
    queryset = Info_about_cilinc.objects.all()
    serializers_class = Info_about_cilincSerializers

"""  Finished CRUD model  """