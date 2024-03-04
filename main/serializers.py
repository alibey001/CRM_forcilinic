from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )


class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class IncomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class RavenueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ravenue
        fields = '__all__'


class CassaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cassa
        fields = '__all__'


class OperationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EquipmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class Info_about_cilincSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info_about_cilinc
        fields = '__all__'

