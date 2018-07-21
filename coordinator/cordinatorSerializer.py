from rest_framework import serializers
from .models import CoordinatorAnaucements
from system_tables.models import SysteamControl
from students.models import StudentGroups
from students.models import GroupsProject
from students.models import Message
from .models import Coordinator
from supervisor.models import ReceivedConcept
from system_tables.models import Login
from supervisor.models import Panel
class AnaucementSerializers(serializers.ModelSerializer):


     class Meta:
         model=CoordinatorAnaucements
         fields=('coordinator_employee_id','title','creted_at','description')
class CurentStatesOfSystemControlSerializer(serializers.ModelSerializer):
    class Meta:
        model=SysteamControl
        exclude=['id']
class TitleAndConceptNpte(serializers.ModelSerializer):
    class Meta:
        model = GroupsProject
        fields = ( 'title', 'concept_note')
class ListRejectedConceptNoteSerializer(serializers.ModelSerializer):
    group_title  = TitleAndConceptNpte()

    class Meta:
        model=StudentGroups
        fields=('group_title','proposed_supervisor','group_id')
class SeeReasonsForRejectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReceivedConcept
        fields=['reasons']
class DestroyStudentMessageAfterAcceptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields="__all__"
class UpdateProfilPicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coordinator
        fields=['profile_picture']
class UpdateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coordinator
        fields=['name']
class UpdateEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coordinator
        fields=['email']
class UpdatePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=['password']
class CreateSupervisorPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Panel
        fields=['first_supervisor','second_supervisor','third_supervisor','fourth_supervisor','fifth_supervisor','six_supervisor','seven_supervisor','eight_supervisor']

class UpdatePanelStudentGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Panel
        fields=['first_groupid','second_groupid','third_groupid','fourth_groupid','fifth_groupid','six_groupid','seven_groupid','eight_groupid','nine_groupid','ten_groupid']
