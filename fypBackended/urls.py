"""fypBackended URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from system_tables import syteam_table_urls
from coordinator import coordinatorUrls
from supervisor import supervisorUrls
from students import student_urls
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include(syteam_table_urls)),
    url(r'^cord/', include(coordinatorUrls)),
    url(r'^super/', include(supervisorUrls)),
    url(r'^std/', include(student_urls)),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Finaly Year Management System Administration'