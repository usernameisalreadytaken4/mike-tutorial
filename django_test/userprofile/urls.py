from django.conf.urls import url
from userprofile import views


urlpatterns = [
    url(r'^profile/$', views.user_profile),

]