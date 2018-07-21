from django.conf.urls import url
from .views import SupervisorReceivedCOnceptNote
from .views import ListReceivedConceptNotes
from .views import UpdateRecomandationOfReceivedConceptNote
from .views import CheckRecomandationConceptNote
from .views import SupervisorSendMessageToStudents
from .views import SupervisorTellReasonsForRejects
from .views import MessageFromStudent
from .views import ViewMyGroup
from .views import ViewMyMessageFromStudent
from .views import SupervisorReadedMessage
from .views import UnreadedMessages
from .views import SupervisorViewSubmitedReports
from .views import updateEmail
from .views import updateName
from .views import UpdateExperties
from .views import UpdatePhoneNo
from .views import UpdateOfficeNumber
from .views import UpdateOfficeImageProfile
from .views import updatePassword

urlpatterns = [
    # update password
    url(r'^updatePassword/(?P<user_id>[\w-]+)', updatePassword.as_view()),
    # update profile image
    url(r'^updateprofileImage/(?P<employee_id>[\w-]+)', UpdateOfficeImageProfile.as_view()),
    # update officeNumber
    url(r'^UpdateOfficeNumber/(?P<employee_id>[\w-]+)', UpdateOfficeNumber.as_view()),
    # upate phoneNumber
    url(r'^UpdatePhoneNo/(?P<employee_id>[\w-]+)', UpdatePhoneNo.as_view()),
    # update experties
    url(r'^UpdateExperties/(?P<employee_id>[\w-]+)', UpdateExperties.as_view()),
    # update name
    url(r'^updateName/(?P<employee_id>[\w-]+)', updateName.as_view()),
    # update email
    url(r'^updateEmail/(?P<employee_id>[\w-]+)', updateEmail.as_view()),
    # supervisor view submited reports
    url(r'^submitedreports', SupervisorViewSubmitedReports.as_view()),
     # unreadedMessages
    url(r'^UnreadedMessages', UnreadedMessages.as_view()),
    # supervisor update readed messages
    url(r'^updatereadedmessages', SupervisorReadedMessage.as_view()),
    # supervisor view his Group
      # supervisor view his message from student
    url(r'^viewMyMessage', ViewMyMessageFromStudent.as_view()),
    # supervisor view his Group
    url(r'^viewMyGroup', ViewMyGroup.as_view()),
     # supervisor get message from student
    url(r'^createmessageforsupervisor', MessageFromStudent.as_view()),
    # supervisor tellReasons for Rejections
    url(r'^sendmessageforRejection/(?P<group_id>[\w-]+)', SupervisorTellReasonsForRejects.as_view()),
    # supervisor send message to students
    url(r'^sendmessage', SupervisorSendMessageToStudents.as_view()),
    # checkRecomandation of conceptNote
    url(r'^recoamandatio', CheckRecomandationConceptNote.as_view()),
    # create supervisorReceived COnceptNote
    url(r'^createSupervisorConceptNote', SupervisorReceivedCOnceptNote.as_view()),
    #get title and ConceptNote for prposedSUpervisor
    url(r'^getileandConceptNote',ListReceivedConceptNotes.as_view()),
    #supervisor upadate recomandations of received Concept Note
    url(r'^updateconeptnoterecomandations/(?P<group_id>[\w-]+)', UpdateRecomandationOfReceivedConceptNote.as_view()),
    ]