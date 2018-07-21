from django.contrib import admin
from .models import Supervisor
from .models import MessageFromSudents
from .models import ReceivedConcept
from .models import Panel

admin.site.register(Supervisor)
admin.site.register(MessageFromSudents)
admin.site.register(ReceivedConcept)
admin.site.register(Panel)

