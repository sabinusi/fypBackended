from rest_framework import serializers
from .models import ReceivedConcept
from .models import MessageFromSudents
from .models import MessageFromSudents
from students.models import Message
from students.models import StudentGroups
from students.models import GroupsProject
from .models import Supervisor
from  system_tables.models import Login


class SupervisorReceivedCOnceptNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReceivedConcept
        fields=('supervisor_employee_id','group_id')
class UpdateRecomandationOfReceivedConceptNoteSerializers(serializers.ModelSerializer):
    class Meta:

        model=ReceivedConcept
        fields=['recomandation']
class RecomandationOfReceivedConceptNoteSerializers(serializers.ModelSerializer):
    class Meta:

        model=ReceivedConcept
        fields=['group_id']
class SendMessageToStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=('student_group_id','message_from_supervisor')
class UpdateReasonForRejectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReceivedConcept
        fields = ['reasons']

class MessageFromStudentSerilizer(serializers.ModelSerializer):
    class Meta:
        model=MessageFromSudents
        exclude=['id']
class ViewMyGroupDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=GroupsProject
        fields=('title','concept_note')
class ViewMyGroupSerializer(serializers.ModelSerializer):
    group_title=ViewMyGroupDataSerializer()
    class Meta:
        model=StudentGroups
        fields=('group_id','first_member_reg_no','second_member_reg_no','third_member_reg_no','group_title')
class SupervisorReadedMessageSeralizer(serializers.ModelSerializer):
    class Meta:
        model=MessageFromSudents
        fields=['readed']
class supervisorViewSubmitedReportsOtherDatas(serializers.ModelSerializer):
    class Meta:
        model=GroupsProject
        fields=('group_id','title','semister1_progress','semister1_final','semister2_progress','semister2_Final')
class SupervisorViewSubmitedReportsSerializer(serializers.ModelSerializer):
    group_title=supervisorViewSubmitedReportsOtherDatas()
    class Meta:
        model=StudentGroups
        fields=['group_title']
class updateEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supervisor
        fields=['email']
class UpdateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supervisor
        fields=['name']
class UpdateExpertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supervisor
        fields=['experties']
class UpdatePhoneNoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supervisor
        fields=['phone_number']
class UpdateOfficeNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supervisor
        fields=['ofice_number']

class UpdateOfficeImageProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supervisor
        fields=['profile_picture']
class updatePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=['password']