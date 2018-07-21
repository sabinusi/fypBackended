from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .supervisorSerilizer import SupervisorReceivedCOnceptNoteSerializer
from  .models import ReceivedConcept
from students.studentSerializers import getTitleAndConceptnoteForsepecficSupervisor
from students.models import StudentGroups
from .supervisorSerilizer import UpdateRecomandationOfReceivedConceptNoteSerializers
from .supervisorSerilizer import RecomandationOfReceivedConceptNoteSerializers
from .supervisorSerilizer import SendMessageToStudentsSerializer
from .supervisorSerilizer import UpdateReasonForRejectionsSerializer
from .supervisorSerilizer import MessageFromStudentSerilizer
from .supervisorSerilizer import ViewMyGroupSerializer
from .supervisorSerilizer import SupervisorReadedMessageSeralizer
from .supervisorSerilizer import SupervisorViewSubmitedReportsSerializer
from students.models import Message
from .models import MessageFromSudents
from .supervisorSerilizer import updateEmailSerializer
from .supervisorSerilizer import UpdateNameSerializer
from .supervisorSerilizer import UpdateExpertiesSerializer
from .supervisorSerilizer import UpdatePhoneNoSerializer
from .supervisorSerilizer import UpdateOfficeNumberSerializer
from .supervisorSerilizer import UpdateOfficeImageProfileSerializer
from .supervisorSerilizer import updatePasswordSerializer
from system_tables.models import Login

from  .models import Supervisor

class SupervisorReceivedCOnceptNote(generics.CreateAPIView):
    queryset = ReceivedConcept
    serializer_class = SupervisorReceivedCOnceptNoteSerializer
class ListReceivedConceptNotes(generics.ListAPIView):
    def get_queryset(self):
        id = self.request.query_params.get('employeeID', None)
        if id is not None:
            queryset = StudentGroups.objects.filter(proposed_supervisor=id)
        return queryset
    serializer_class=getTitleAndConceptnoteForsepecficSupervisor
class UpdateRecomandationOfReceivedConceptNote(generics.UpdateAPIView):
    serializer_class = UpdateRecomandationOfReceivedConceptNoteSerializers
    queryset = ReceivedConcept.objects.all()
    lookup_field = 'group_id'
class CheckRecomandationConceptNote(generics.ListAPIView):
    def get_queryset(self):
        id = self.request.query_params.get('recom', None)
        if id is not None:
            queryset = ReceivedConcept.objects.filter(recomandation=id)
        return queryset
    serializer_class=RecomandationOfReceivedConceptNoteSerializers

class SupervisorSendMessageToStudents(generics.CreateAPIView):
    queryset = Message
    serializer_class = SendMessageToStudentsSerializer
class SupervisorTellReasonsForRejects(generics.UpdateAPIView):
    queryset = ReceivedConcept
    serializer_class = UpdateReasonForRejectionsSerializer
    lookup_field = 'group_id'
class MessageFromStudent(generics.CreateAPIView):
    serializer_class=MessageFromStudentSerilizer
    queryset=MessageFromSudents.objects.all()
class ViewMyGroup(generics.ListAPIView):
    def get_queryset(self):
        id_list = self.request.query_params.get('id')
        id_listt=id_list.split(',')
        if id_list is not None:
            queryset = StudentGroups.objects.filter(group_id__in=id_listt)
        return queryset
    serializer_class=ViewMyGroupSerializer


class ViewMyMessageFromStudent(generics.ListAPIView):
    def get_queryset(self):
        id_list = self.request.query_params.get('id')
        if id_list is not None:
            queryset = MessageFromSudents.objects.filter(employee_id=id_list)
        return queryset

    serializer_class = MessageFromStudentSerilizer
class SupervisorReadedMessage(generics.ListAPIView):
    serializer_class = SupervisorReadedMessageSeralizer

    def get_queryset(self):
        id_list = self.request.query_params.get('id')

        if id_list is not None:
            queryset = MessageFromSudents.objects.filter(employee_id=id_list,readed=False)
            for s in queryset:
                s.readed=True
                s.save()
        return queryset
class UnreadedMessages(generics.ListAPIView):
    serializer_class = SupervisorReadedMessageSeralizer

    def get_queryset(self):
        id_list = self.request.query_params.get('id')

        if id_list is not None:
            queryset = MessageFromSudents.objects.filter(employee_id=id_list, readed=False)
        return queryset
class SupervisorViewSubmitedReports(generics.ListAPIView):
    serializer_class = SupervisorViewSubmitedReportsSerializer

    def get_queryset(self):
        id_list = self.request.query_params.get('id')

        if id_list is not None:
            queryset = StudentGroups.objects.filter(supervisor_employee_id=id_list)
        return queryset
class updateEmail(generics.UpdateAPIView):
    serializer_class = updateEmailSerializer
    queryset = Supervisor.objects.all()
    lookup_field = 'employee_id'
class updateName(generics.UpdateAPIView):
    serializer_class = UpdateNameSerializer
    queryset = Supervisor.objects.all()
    lookup_field = 'employee_id'

class UpdateExperties(generics.UpdateAPIView):
    serializer_class = UpdateExpertiesSerializer
    queryset = Supervisor.objects.all()
    lookup_field = 'employee_id'

class UpdatePhoneNo(generics.UpdateAPIView):
    serializer_class = UpdatePhoneNoSerializer
    queryset = Supervisor.objects.all()
    lookup_field = 'employee_id'

class UpdateOfficeNumber(generics.UpdateAPIView):
    serializer_class = UpdateOfficeNumberSerializer
    queryset = Supervisor.objects.all()
    lookup_field = 'employee_id'

class UpdateOfficeImageProfile(generics.UpdateAPIView):
    serializer_class = UpdateOfficeImageProfileSerializer
    queryset = Supervisor.objects.all()
    lookup_field = 'employee_id'

class updatePassword(generics.UpdateAPIView):
    serializer_class = updatePasswordSerializer
    queryset = Login.objects.all()
    lookup_field = 'user_id'