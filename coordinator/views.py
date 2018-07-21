from django.shortcuts import render
from .cordinatorSerializer import AnaucementSerializers
from .cordinatorSerializer import CurentStatesOfSystemControlSerializer
from .cordinatorSerializer import ListRejectedConceptNoteSerializer
from rest_framework import generics
from .models import CoordinatorAnaucements
from system_tables.models import SysteamControl
from supervisor.models import ReceivedConcept
from students.models import StudentGroups
from students.models import Message
from .cordinatorSerializer import SeeReasonsForRejectionSerializer
from .cordinatorSerializer import DestroyStudentMessageAfterAcceptSerializer
from .cordinatorSerializer import UpdateProfilPicSerializer
from .models import Coordinator
from .cordinatorSerializer import UpdateNameSerializer
from .cordinatorSerializer import UpdateEmailSerializer
from .cordinatorSerializer import UpdatePasswordSerializer
from .cordinatorSerializer import CreateSupervisorPanelSerializer
from .cordinatorSerializer import UpdatePanelStudentGroupsSerializer
from system_tables.models import Login
from supervisor.models import Panel


class AnaucementCreate(generics.CreateAPIView):
    queryset = CoordinatorAnaucements
    serializer_class = AnaucementSerializers
class CurentStatesOfSystemControl(generics.ListAPIView):
    queryset = SysteamControl.objects.all()
    serializer_class = CurentStatesOfSystemControlSerializer
class ListRejectedConceptNote(generics.ListAPIView):
    def get_queryset(self):
        id_list = self.request.query_params.get('id')
        id_listt=id_list.split(',')
        if id_list is not None:
            queryset = StudentGroups.objects.filter(group_id__in=id_listt)
        return queryset
    serializer_class=ListRejectedConceptNoteSerializer

class SeeReasonsForRejection(generics.RetrieveAPIView):
    queryset = ReceivedConcept.objects.all()
    serializer_class = SeeReasonsForRejectionSerializer
    lookup_field = 'group_id'

class DestroyStudentMessageAfterAccept(generics.DestroyAPIView):
    serializer_class=DestroyStudentMessageAfterAcceptSerializer
    lookup_field='student_group_id'
    queryset = Message.objects.all()

class UpdateProfilPic(generics.UpdateAPIView):
    serializer_class = UpdateProfilPicSerializer
    queryset = Coordinator.objects.all()
    lookup_field = 'employee_id'
class UpdateName(generics.UpdateAPIView):
    serializer_class = UpdateNameSerializer
    queryset = Coordinator.objects.all()
    lookup_field = 'employee_id'
class UpdateEmail(generics.UpdateAPIView):
    serializer_class = UpdateEmailSerializer
    queryset = Coordinator.objects.all()
    lookup_field = 'employee_id'
class UpdatePassword(generics.UpdateAPIView):
    serializer_class = UpdatePasswordSerializer
    queryset = Login.objects.all()
    lookup_field = 'user_id'

class CreateSupervisorPanel(generics.CreateAPIView):
    queryset = Panel.objects.all()
    serializer_class = CreateSupervisorPanelSerializer


class UpdatePanelStudentGroups(generics.UpdateAPIView):
    serializer_class = UpdatePanelStudentGroupsSerializer
    queryset = Panel.objects.all()
    lookup_field = 'panel_id'