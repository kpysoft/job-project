from django.conf.urls import url
from jobapp import views

urlpatterns=[

url(r'^bangalore',views.bangalorejob),
url(r'^surat', views.suratjob),
url(r'^pune', views.punejob),


]
