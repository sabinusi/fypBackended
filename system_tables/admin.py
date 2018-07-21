from django.contrib import admin
from system_tables.models import Login
from .models import PastProjects
from .models import SysteamControl
admin.site.register(Login)
admin.site.register(PastProjects)
admin.site.register(SysteamControl)
