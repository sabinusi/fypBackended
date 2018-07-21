from django.contrib import admin
from  .models import Student
from  .models import StudentGroups
from  .models import GroupsProject
from  .models import MessageFromCoordinator

from  .models import Message

admin.site.register(Student)
admin.site.register(StudentGroups)
admin.site.register(GroupsProject)

admin.site.register(Message)
admin.site.register(MessageFromCoordinator)

