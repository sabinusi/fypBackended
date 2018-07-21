from coordinator.models import CoordinatorAnaucements
from supervisor.models import Supervisor
from rest_framework import serializers
from .models import Message
from system_tables.models import PastProjects
from .models import GroupsProject
from .models import Student
from .models import StudentGroups
from rest_framework.views import APIView
from supervisor.models import MessageFromSudents
from coordinator.models import Coordinator
from system_tables.models import SysteamControl
from system_tables.models import Login





class StudentPicSerializerrs(serializers.ModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     remove_fields = kwargs.pop('remove_fields', None)
    #     super(StudentSerializerrs, self).__init__(*args, **kwargs)
    #
    #     if remove_fields:
    #         # for multiple fields in a list
    #         for field_name in remove_fields:
    #             self.fields.pop(field_name)


    class Meta:
        model=Student
        fields=['profile_picture']
class CordinatorSerializerOtherdatasForAnaucement(serializers.ModelSerializer):
    class Meta:
        model=Coordinator
        fields=('profile_picture','name')


class SudentSerializeAnnaucements(serializers.ModelSerializer):
    coordinator_employee_id=CordinatorSerializerOtherdatasForAnaucement(read_only=True)

    class Meta:
        model = CoordinatorAnaucements
        fields = ('title', 'description', 'creted_at','coordinator_employee_id')


class SupervisotSerializedList(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ('name', 'email', 'phone_number', 'ofice_number', 'experties')


class PasprojectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastProjects
        fields = ('title', 'conceptNote', 'year')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('student_id', 'message_from_supervisor', 'message_from_coordinator')


class ViewSubmitedReportSerialization(serializers.ModelSerializer):
    class Meta:
        model = GroupsProject

        fields = ('semister1_progress', 'semister1_final', 'semister2_progress', 'semister2_Final')

class ProfileSerialization(serializers.ModelSerializer):

    class Meta:
        model = StudentGroups
        fields = ('first_member_reg_no', 'second_member_reg_no', 'third_member_reg_no', 'supervisor_employee_id')


class ChangeConceptNoteSerializer(serializers.ModelSerializer):
       class Meta:
        model = GroupsProject
        fields = ('concept_note', 'title')

class StudentGetConceptnoteOncreate(serializers.ModelSerializer):

    class Meta:
        model=GroupsProject
        fields=['concept_note','title']

class SubmiteConceptNoteGroupcreation(serializers.ModelSerializer):
    group_title=StudentGetConceptnoteOncreate()

    class Meta:
        model=StudentGroups

        fields=('first_member_reg_no','second_member_reg_no','third_member_reg_no','group_title','proposed_supervisor')

    def create(self, validated_data):
        groupsproject_data = validated_data.pop('group_title')
        studentsGroups = StudentGroups.objects.create(**validated_data)
        GroupsProject.objects.create( **groupsproject_data)
        return StudentGroups

class StudentUpdateProposedSupervisor(serializers.ModelSerializer):
    class Meta:
         model=StudentGroups
         fields=['proposed_supervisor']
class StudentSendMessageTosupervisor(serializers.ModelSerializer):
    class Meta:
        model=MessageFromSudents
        fields="__all__"
class StudentViewSupervisorWithExperties(serializers.ModelSerializer):
    class Meta:
        model=Supervisor
        fields=('name','experties')
class StudentNameAndRegNo(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('firstname','lastname','student_reg_no')

class StudentGetId(serializers.ModelSerializer):
    class Meta:
        model=StudentGroups
        fields=['group_id']
class StudentUpdateGroupId(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['studentgroup']
class StudentUpadateTitle(serializers.ModelSerializer):
    class Meta:
     model=GroupsProject
     fields=['title']
class StudentListGroups(serializers.ModelSerializer):
    group_title = StudentGetConceptnoteOncreate()
    class Meta:
        model = StudentGroups

        fields = (
        'first_member_reg_no', 'second_member_reg_no', 'third_member_reg_no', 'group_title', 'proposed_supervisor')
class updateConceptNote(serializers.ModelSerializer):
    class Meta:
        model=GroupsProject
        fields=['concept_note']
class controlsOfConceptNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=SysteamControl
        fields=['submitConceptNote']
class controlsOfreportsSerializers(serializers.ModelSerializer):
    class Meta:
        model=SysteamControl
        fields=('sem1progress','sem1final','sem2progress','sem2final')
class updateSemister1ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model=GroupsProject
        fields=['semister1_progress']
class viewOfSubmitedReports(serializers.ModelSerializer):
    class Meta:
     model=GroupsProject
     fields=('semister1_progress','semister1_final','semister2_progress','semister2_Final')

class updateSem2finalReportSerilizer(serializers.ModelSerializer):
    class Meta:
        model=GroupsProject
        fields=['semister2_Final']
class updateSem1finalReportSerilizer(serializers.ModelSerializer):
    class Meta:
        model=GroupsProject
        fields=['semister1_final']
class updateSem2ProgressReportSerilizer(serializers.ModelSerializer):
    class Meta:
        model=GroupsProject
        fields=['semister2_progress']
class studentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('student_reg_no','firstname','lastname')
class updateSecondMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentGroups
        fields=['second_member_reg_no']
class updateThirdMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentGroups
        fields=['third_member_reg_no']
class updatePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=['password']
class updateEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['email']

class getSupervisorEmployeeIdSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supervisor
        fields=['employee_id']
class StudentGetConceptnoteOncreateForSupervisor(serializers.ModelSerializer):

    class Meta:
        model=GroupsProject
        fields=['concept_note','title','group_id']
class getTitleAndConceptnoteForsepecficSupervisor(serializers.ModelSerializer):
    group_title = StudentGetConceptnoteOncreateForSupervisor()

    class Meta:
        model = StudentGroups
        # fields = ['group_title','first_member_reg_no','second_member_reg_no','third_member_reg_no']
        fields = ['group_title']
class UpdateSupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentGroups
        fields=['supervisor_employee_id']
class SupervisorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supervisor
        fields=['name']

class ViewMessageFromSupervisorSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=('message_from_supervisor','creted_at')
class getBothSupervisorEmployeeSerilizers(serializers.ModelSerializer):
    class Meta:
        model=StudentGroups
        fields=('supervisor_employee_id','proposed_supervisor')

class DataForSendingMessageToSuperisor(serializers.ModelSerializer):

    class Meta:
        model=GroupsProject
        fields=['title']
class updateStudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['studentgroup']
class updatefirstnameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['firstname']
class updatelastnameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['lastname']
class updatecourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['course']
class viewEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['email']