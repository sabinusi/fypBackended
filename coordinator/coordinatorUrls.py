from django.conf.urls import url
from .views import AnaucementCreate
from .views import CurentStatesOfSystemControl
from .views import ListRejectedConceptNote
from .views import SeeReasonsForRejection
from .views import DestroyStudentMessageAfterAccept
from .views import UpdateProfilPic
from .views import UpdateName
from .views import UpdateEmail
from .views import UpdatePassword
from .views import CreateSupervisorPanel
from .views import UpdatePanelStudentGroups

from  students.views import UpdateControlsReportsUpdates


urlpatterns = [
     # update student groups to panel
    url(r'^UpdatePanelStudentGroups/(?P<panel_id>[\w-]+)', UpdatePanelStudentGroups.as_view()),
     # create supervisor for panel
    url(r'^CreateSupervisorPanel', CreateSupervisorPanel.as_view()),
     # update password
     url(r'^UpdatePassword/(?P<user_id>[\w-]+)', UpdatePassword.as_view()),
     # update email
    url(r'^UpdateEmail/(?P<employee_id>[\w-]+)', UpdateEmail.as_view()),
     # update name
   url(r'^UpdateName/(?P<employee_id>[\w-]+)', UpdateName.as_view()),
     # upate profile picture
    url(r'^profilePic/(?P<employee_id>[\w-]+)', UpdateProfilPic.as_view()),
     # destroy student message
    url(r'^destroystdmessage/(?P<student_group_id>[\w-]+)', DestroyStudentMessageAfterAccept.as_view()),
    # see reason for rejection
    url(r'^seereasonforrejection/(?P<group_id>[\w-]+)', SeeReasonsForRejection.as_view()),
    # retrive data of rejected conceptNotes
    url(r'^dataofrejectedconceptnote', ListRejectedConceptNote.as_view()),
    #current state of system
    url(r'^currentStateOfSystem',CurentStatesOfSystemControl.as_view()),
    url(r'^postanaucemnt',AnaucementCreate.as_view()),
    # updatesof of reports submission
    url(r'^alowreports/(?P<id>[\w-]+)',UpdateControlsReportsUpdates.as_view()),
]

