from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Login
from students.studentSerializers import StudentPicSerializerrs
from students.models import Student
from .systeam_table_serializers import StudentLoginSerializers
from .systeam_table_serializers import SupervisorLoginSerializers
from .systeam_table_serializers import CordinatorLoginSerializers
from supervisor.models import Supervisor
from coordinator.models import Coordinator
from .systeam_table_serializers import forgetPasswordSerializer
import smtplib


class forgetPassword(generics.ListAPIView):
    serializer_class = forgetPasswordSerializer
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        if id is not None:
            def email(a,b):
                if b =='student':
                    std = Student.objects.get(student_reg_no=a).email
                    return std
                elif b=='supervisor':
                    sup = Supervisor.objects.get(employee_id=a).email
                    return sup
                elif b=='coordinator':
                    cord = Coordinator.objects.get(employee_id=a).email
                    return cord

            ui=Login.objects.get(user_id=id).password
            role=Login.objects.get(user_id=id).role

            server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
            server.login('sabinusimlambo@gmail.com', 'sabinusia')

            server.sendmail('sabinusimlambo@gmail.com', email(id,role), 'youre recover password from FYPMS is '+ui)
            mi=Login.objects.filter(user_id=id)
            return  mi





class LoginListApiview(generics.ListAPIView):
     def get_serializer_class(self):
         id = self.request.query_params.get('id', None)
         password = self.request.query_params.get('pass', None)
         user = Login.objects.get(user_id=id, password=password)
         if user.role=='student':
             return StudentLoginSerializers
         elif user.role=='supervisor':
             return SupervisorLoginSerializers
         elif user.role=='cordinator':
             return CordinatorLoginSerializers


     def get_queryset(self):
         id = self.request.query_params.get('id', None)
         password= self.request.query_params.get('pass', None)
         user=Login.objects.get(user_id=id,password=password)
         if user.role == 'student':
             queryset=Student.objects.filter(student_reg_no=id)
         elif user.role=='supervisor':
             queryset=Supervisor.objects.filter(employee_id=id)
         elif user.role=='cordinator':
             queryset=Coordinator.objects.filter(employee_id=id)

         return  queryset










