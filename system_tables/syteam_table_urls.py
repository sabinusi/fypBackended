from .views import LoginListApiview
from .views import forgetPassword
from django.conf.urls import url
urlpatterns = [
    url(r'^l',LoginListApiview.as_view() ),
     url(r'^getpassword',forgetPassword.as_view() )


]