from rest_framework import serializers
from coordinator.models import Coordinator
from supervisor.models import Supervisor
from students.models import Student
from .models import Login

class StudentLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('student_reg_no','firstname','profile_picture','role','studentgroup','email','course','lastname')
class SupervisorLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model=Supervisor
        fields=('name','employee_id','profile_picture','role','email','phone_number','experties','ofice_number')
class CordinatorLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model=Coordinator
        fields=('employee_id','name','profile_picture','role','email')


class forgetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=('user_id','role')