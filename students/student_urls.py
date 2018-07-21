from .views import StudentAnnaucementList
from .views import SupervisorList
from .views import PasprojectsList
from .views import MessageList
from .views import ViewSubmitedList
from django.conf.urls import url
from .views import ProfileListView
from .views import ResubmiteConceptNote
from  .views import StudentProfilePic
from  .views import StudentCreateGroupAndConcept
from  .views import StudentUpdateProposedSupervisor
from  .views import SendMessageToSupervisor
from  .views import ViewSuperNameAndExperties
from  .views import GetNameAndReg
from  .views import GetIdSerializer
from  .views import UpdateStudentGroupIdSerilizer
from  .views import StudentUpdatesTitle
from  .views import StudentListGroupsData
from  .views import StudentUpdateConcetNote
from  .views import SupervisorAlowCOnceptNote
from  .views import GetSupervisorControlOnConceptNote
from  .views import ListReportsConrols
from  .views import updateSe1ProgressRe
from  .views import ViewOfSubmitedReportSerializers
from  .views import updateSemister1final
from  .views import updateSemister2final
from  .views import updateSemister2Progress
from  .views import ListStudentName
from  .views import updateSecondMemberOfGroup
from  .views import updateThirdMemberOfGroup
from  .views import updatePassword
from  .views import updateEmail
from  .views import getSupervisorEmployeeId
from  .views import GetStudentDataAfterGreateGroup
from  .views import getMySUperWIthExpertie
from  .views import StudentUpdateSupervisor
from  .views import StudentGetSupervisorName
from  .views import ViewMessageFromSupervisors
from  .views import getBothSupervisorEmployee
from  .views import DataForSendingMessageToSuperisorFromSudent
from  .views import updateStudentGroup
from  .views import updatefirstname
from  .views import updatelastname
from  .views import updatecourse
from  .views import viewEmail






urlpatterns = [
    #  view email
   url(r'^email', viewEmail.as_view()),
    # update course
    url(r'^updatecourse/(?P<student_reg_no>[\w-]+)', updatecourse.as_view()),
    # update lastname
    url(r'^updatelastname/(?P<student_reg_no>[\w-]+)', updatelastname.as_view()),
    #update firstname
   url(r'^updatefirstname/(?P<student_reg_no>[\w-]+)', updatefirstname.as_view()),
    # student update his group to null by attempt to left it
    url(r'^updateStudentgroup/(?P<student_reg_no>[\w-]+)', updateStudentGroup.as_view()),
   # student datas for sending message
    url(r'^messagedata/(?P<group_id>[\w-]+)', DataForSendingMessageToSuperisorFromSudent.as_view()),
    # student view supervisors id's
    url(r'^viewsupervisorsid/(?P<group_id>[\w-]+)', getBothSupervisorEmployee.as_view()),
    #student view messages from supervisors
    url(r'^viewsupervisormessage', ViewMessageFromSupervisors.as_view()),
    #student get supervisor name
    url(r'^getsupervisorname/(?P<employee_id>[\w-]+)', StudentGetSupervisorName.as_view()),
    #update supervisor by proposed supervisor
    url(r'^updatesupervisor/(?P<group_id>[\w-]+)', StudentUpdateSupervisor.as_view()),
    # get supervisor name and experties by using employee id
    url(r'^getMysupervisor/(?P<employee_id>[\w-]+)', getMySUperWIthExpertie.as_view()),
    #get supervisor employee id
    url(r'^getnewstudentdata/(?P<student_reg_no>[\w-]+)',GetStudentDataAfterGreateGroup.as_view()),
    #get supervisor employee id
    url(r'^getsupervisorid',getSupervisorEmployeeId.as_view()),
    #update email
    url(r'^updateEmail/(?P<student_reg_no>[\w-]+)',updateEmail.as_view()),
    #update password
    url(r'^updatepassword/(?P<user_id>[\w-]+)',updatePassword.as_view()),
    # update semister 2 final
    url(r'^updatesemister2final/(?P<group_id>[\w-]+)',updateSemister2final.as_view()),

    # update 3rd member of group
    url(r'^updatethirdmember/(?P<group_id>[\w-]+)', updateThirdMemberOfGroup.as_view()),
    # update semister 2 final
    url(r'^updatesecondmember/(?P<group_id>[\w-]+)', updateSecondMemberOfGroup.as_view()),
    # give a studenet names with regNo
    url(r'^getnames', ListStudentName.as_view()),
# update semister 2 final
    url(r'^updatesemister2progress/(?P<group_id>[\w-]+)',updateSemister2Progress.as_view()),
    # update semister 1 final
    url(r'^updatesemister1final/(?P<group_id>[\w-]+)', updateSemister1final.as_view()),
    # update semister on progress reports
    url(r'^updateSemis1ProgressReport/(?P<group_id>[\w-]+)',updateSe1ProgressRe.as_view()),
    # view reports
    url(r'^seereports',ViewOfSubmitedReportSerializers.as_view()),

    url(r'^annaucements',StudentAnnaucementList.as_view()),
    url(r'^supervisors',SupervisorList.as_view()),
    url(r'^pastprojects',PasprojectsList.as_view()),
    # //get id of group for update
    url(r'^getid',GetIdSerializer.as_view()),

    #list conrols of the systeamspi
    url(r'^listgroupcontrols',ListReportsConrols.as_view()),
    # update student group id
    url(r'^updategroupid/(?P<student_reg_no>[\w-]+)/$',UpdateStudentGroupIdSerilizer.as_view()),

    # updates of group title
    url(r'^updatetile/(?P<group_id>[\w-]+)',StudentUpdatesTitle.as_view()),
    # listGroupsData
    url(r'^listGroupsData',StudentListGroupsData.as_view()),
    #update supervisor conceptNoteControl
    url(r'^updateConceptNote/(?P<id>[\w-]+)',SupervisorAlowCOnceptNote.as_view()),
    # update concept note
    url(r'^conceptNoteUpdate/(?P<group_id>[\w-]+)',StudentUpdateConcetNote.as_view()),
    #show supervisor control
    url(r'^supervisorcontrolConceptNote',GetSupervisorControlOnConceptNote.as_view()),

    url(r'^message',MessageList.as_view()),
    url(r'^SendmessageToSupervisor',SendMessageToSupervisor.as_view()),
    url(r'^superWithExperties',ViewSuperNameAndExperties.as_view()),
    url(r'^getNameAndReg',GetNameAndReg.as_view()),

    url(r'^viewsubmitedreport/(?P<group_id>[\w-]+)/$',ViewSubmitedList.as_view()),
    url(r'^profilepic/(?P<student_reg_no>[\w-]+)',StudentProfilePic.as_view()),
    url(r'^creategoupandconceptnote',StudentCreateGroupAndConcept.as_view()),
    url(r'^profile',ProfileListView.as_view()),
    url(r'^update_proposed_supervisor/(?P<group_id>[\w-]+)',StudentUpdateProposedSupervisor.as_view()),
    url(r'^conceptnote/(?P<group_id>[\w-]+)/update/$',ResubmiteConceptNote.as_view()),


]