from django.shortcuts import render
from .studentSerializers import SudentSerializeAnnaucements
from .studentSerializers import SupervisotSerializedList
from coordinator.models import CoordinatorAnaucements
from supervisor.models import Supervisor
from  .studentSerializers import PasprojectsSerializer
from system_tables.models import PastProjects
from  .models import Message
from  .studentSerializers import MessageSerializer
from  .studentSerializers import ViewSubmitedReportSerialization
from .models import GroupsProject
from .models import Student
from  rest_framework.response import Response
from .models import StudentGroups
from .studentSerializers import ProfileSerialization
from rest_framework.views import APIView
from .studentSerializers import ChangeConceptNoteSerializer
from .models import GroupsProject
from .studentSerializers import StudentPicSerializerrs
from  .studentSerializers import SubmiteConceptNoteGroupcreation
from rest_framework import generics
from  .studentSerializers import StudentUpdateProposedSupervisor
from  supervisor.models import MessageFromSudents
from  .studentSerializers import StudentSendMessageTosupervisor
from  .studentSerializers import StudentViewSupervisorWithExperties
from  .studentSerializers import StudentNameAndRegNo
from  .studentSerializers import StudentGetId
from  .studentSerializers import StudentUpdateGroupId
from  .studentSerializers import StudentUpadateTitle
from  .studentSerializers import StudentListGroups
from  .studentSerializers import updateConceptNote
from  .studentSerializers import controlsOfConceptNoteSerializer
from  system_tables.models import SysteamControl
from  system_tables.models import Login
from  .studentSerializers import controlsOfreportsSerializers
from  .studentSerializers import updateSemister1ProgressSerializer
from  .studentSerializers import viewOfSubmitedReports
from  .studentSerializers import updateSem2finalReportSerilizer
from  .studentSerializers import updateSem1finalReportSerilizer
from  .studentSerializers import updateSem2ProgressReportSerilizer
from  .studentSerializers import studentNameSerializer
from  .studentSerializers import updateSecondMemberSerializer
from  .studentSerializers import updateThirdMemberSerializer
from  .studentSerializers import updatePasswordSerializer
from  .studentSerializers import updateEmailSerializer
from  .studentSerializers import getSupervisorEmployeeIdSerializer
from  .studentSerializers import UpdateSupervisorSerializer
from  .studentSerializers import SupervisorNameSerializer
from  .studentSerializers import ViewMessageFromSupervisorSerilizer
from  .studentSerializers import getBothSupervisorEmployeeSerilizers
from  .studentSerializers import DataForSendingMessageToSuperisor
from  .studentSerializers import updateStudentGroupSerializer
from  .studentSerializers import updatefirstnameSerializer
from  .studentSerializers import updatelastnameSerializer
from  .studentSerializers import updatecourseSerializer
from  .studentSerializers import viewEmailSerializer
from django.db.models import Q
from system_tables.systeam_table_serializers import StudentLoginSerializers


class viewEmail(generics.ListAPIView):
    def get_queryset(self):

        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = Student.objects.filter(student_reg_no=id)
        return queryset

    serializer_class = viewEmailSerializer

class updatecourse(generics.UpdateAPIView):
    serializer_class = updatecourseSerializer
    queryset = Student.objects.all()
    lookup_field = 'student_reg_no'
class updatefirstname(generics.UpdateAPIView):
    serializer_class = updatefirstnameSerializer
    queryset = Student.objects.all()
    lookup_field = 'student_reg_no'


class updatelastname(generics.UpdateAPIView):
    serializer_class = updatelastnameSerializer
    queryset = Student.objects.all()
    lookup_field = 'student_reg_no'


class StudentAnnaucementList(generics.ListAPIView):
    serializer_class = SudentSerializeAnnaucements
    queryset = CoordinatorAnaucements.objects.all().order_by('-creted_at')


class SupervisorList(generics.ListAPIView):
    serializer_class = SupervisotSerializedList
    queryset = Supervisor.objects.all()
class PasprojectsList(generics.ListAPIView):


     def get_queryset(self):
         queryset = Message.objects.all()
         username = self.request.query_params.get('t', None)
         if username is not None:
             queryset = PastProjects.objects.filter(title__contains=username)
         return queryset




     serializer_class = PasprojectsSerializer

class MessageList(generics.ListAPIView):
    serializer_class = MessageSerializer


    def get_queryset(self):

      queryset = Message.objects.all()
      username = self.request.query_params.get('student_id',None)
      if username is not None:
        queryset = queryset.filter(student_id=username)
      return queryset

class ViewSubmitedList(generics.RetrieveAPIView):
    serializer_class = ViewSubmitedReportSerialization
    queryset = GroupsProject.objects.all()
    lookup_field = 'group_id'
class ProfileListView(generics.ListAPIView):
    def get_queryset(self):
        no=self.request.query_params.get('gno',None)
        if no is not None:
            queryset=StudentGroups.objects.filter(pk=no)
        return queryset
    serializer_class = ProfileSerialization


class ResubmiteConceptNote(generics.UpdateAPIView):
    serializer_class = ChangeConceptNoteSerializer
    queryset = GroupsProject.objects.all()
    lookup_field = 'group_id'
class StudentProfilePic(generics.UpdateAPIView):
    serializer_class = StudentPicSerializerrs
    queryset = Student.objects.all()
    lookup_field = 'student_reg_no'
class StudentCreateGroupAndConcept(generics.CreateAPIView):
    serializer_class = SubmiteConceptNoteGroupcreation
    queryset = StudentGroups

class StudentUpdateProposedSupervisor(generics.UpdateAPIView):
    queryset = StudentGroups.objects.all()
    serializer_class = StudentUpdateProposedSupervisor
    lookup_field = 'group_id'

class SendMessageToSupervisor(generics.CreateAPIView):
    queryset = MessageFromSudents
    serializer_class = StudentSendMessageTosupervisor
class ViewSuperNameAndExperties(generics.ListAPIView):
    queryset=Supervisor.objects.all()
    serializer_class=StudentViewSupervisorWithExperties

class GetNameAndReg(generics.ListAPIView):
    queryset=Student.objects.filter(studentgroup=None)
    serializer_class=StudentNameAndRegNo
class GetIdSerializer(generics.ListAPIView):
    def  get_queryset(self):
        id=self.request.query_params.get('id',None)
        if id is not None:
            queryset=StudentGroups.objects.filter(first_member_reg_no=id)
        return  queryset
    serializer_class=StudentGetId


class UpdateStudentGroupIdSerilizer(generics.UpdateAPIView):
    serializer_class=StudentUpdateGroupId
    queryset=Student.objects.all()
    lookup_field = 'student_reg_no'

class StudentUpdatesTitle(generics.UpdateAPIView):
    serializer_class=StudentUpadateTitle
    queryset = GroupsProject.objects.all()
    lookup_field='group_id'


class StudentListGroupsData(generics.ListAPIView):
    serializer_class=StudentListGroups
    def get_queryset(self):

      no = self.request.query_params.get('no',None)
      if no is not None:
        queryset = StudentGroups.objects.filter(group_id=no)
      return queryset
class StudentUpdateConcetNote(generics.UpdateAPIView):
    serializer_class=updateConceptNote;
    queryset = GroupsProject.objects.all()
    lookup_field = 'group_id'
class SupervisorAlowCOnceptNote(generics.UpdateAPIView):
    serializer_class=controlsOfConceptNoteSerializer
    queryset=SysteamControl.objects.all()
    lookup_field='id'
class GetSupervisorControlOnConceptNote(generics.ListAPIView):
    serializer_class=controlsOfConceptNoteSerializer
    queryset=SysteamControl.objects.all()
class ListReportsConrols(generics.ListAPIView):
    queryset=SysteamControl.objects.all()
    serializer_class=controlsOfreportsSerializers
class UpdateControlsReportsUpdates(generics.UpdateAPIView):
    serializer_class = controlsOfreportsSerializers
    queryset = SysteamControl.objects.all()
    lookup_field = 'id'
class updateSe1ProgressRe(generics.UpdateAPIView):
    serializer_class = updateSemister1ProgressSerializer
    queryset = GroupsProject.objects.all()
    lookup_field = 'group_id'
class ViewOfSubmitedReportSerializers(generics.ListAPIView):
    def get_queryset(self):
        no = self.request.query_params.get('gno', None)
        if no is not None:
            queryset = GroupsProject.objects.filter(group_id=no)
        return queryset
    serializer_class=viewOfSubmitedReports
class updateSemister2final(generics.UpdateAPIView):
    serializer_class = updateSem2finalReportSerilizer
    queryset = GroupsProject.objects.all()
    lookup_field = 'group_id'
class updateSemister1final(generics.UpdateAPIView):
    serializer_class = updateSem1finalReportSerilizer
    queryset = GroupsProject.objects.all()
    lookup_field = 'group_id'
class updateSemister2Progress(generics.UpdateAPIView):
    serializer_class = updateSem2ProgressReportSerilizer
    queryset = GroupsProject.objects.all()
    lookup_field = 'group_id'
class ListStudentName(generics.ListAPIView):
    serializer_class = studentNameSerializer

    def get_queryset(self):
        no = self.request.query_params.get('sno', None)
        if no is not None:
            queryset = Student.objects.filter(student_reg_no=no)
        return queryset
class updateSecondMemberOfGroup(generics.UpdateAPIView):
      serializer_class= updateSecondMemberSerializer
      queryset = StudentGroups.objects.all()
      lookup_field = 'group_id'


class updateThirdMemberOfGroup(generics.UpdateAPIView):
    serializer_class = updateThirdMemberSerializer
    queryset = StudentGroups.objects.all()
    lookup_field = 'group_id'
class updatePassword(generics.UpdateAPIView):
    serializer_class = updatePasswordSerializer
    queryset = Login.objects.all()
    lookup_field = 'user_id'

class updateEmail(generics.UpdateAPIView):
    serializer_class = updateEmailSerializer
    queryset = Student.objects.all()
    lookup_field = 'student_reg_no'
class getSupervisorEmployeeId(generics.ListAPIView):
    serializer_class=getSupervisorEmployeeIdSerializer

    def get_queryset(self):
        id = self.request.query_params.get('name', None)
        password = self.request.query_params.get('exp', None)
        user = Supervisor.objects.filter(Q(name=id)& Q( experties=password))
        if user is not None:
            queryset= Supervisor.objects.filter(Q(name=id)& Q( experties=password))
        return queryset
class GetStudentDataAfterGreateGroup(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentLoginSerializers
    lookup_field ='student_reg_no'
class getMySUperWIthExpertie(generics.RetrieveAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = StudentViewSupervisorWithExperties
    lookup_field ='employee_id'

class StudentUpdateSupervisor(generics.UpdateAPIView):
    queryset = StudentGroups.objects.all()
    serializer_class = UpdateSupervisorSerializer
    lookup_field = 'group_id'


class StudentGetSupervisorName(generics.RetrieveAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorNameSerializer
    lookup_field = 'employee_id'
class ViewMessageFromSupervisors(generics.ListAPIView):
    serializer_class = ViewMessageFromSupervisorSerilizer

    def get_queryset(self):
        no = self.request.query_params.get('group_id', None)
        if no is not None:
            queryset = Message.objects.filter(student_group_id=no).order_by('-creted_at')
        return queryset
class getBothSupervisorEmployee(generics.RetrieveAPIView):
    queryset = StudentGroups.objects.all()
    serializer_class = getBothSupervisorEmployeeSerilizers
    lookup_field = 'group_id'

class DataForSendingMessageToSuperisorFromSudent(generics.RetrieveAPIView):
    queryset = GroupsProject.objects.all()
    serializer_class = DataForSendingMessageToSuperisor
    lookup_field = 'group_id'

class updateStudentGroup(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = updateStudentGroupSerializer
    lookup_field = 'student_reg_no'
