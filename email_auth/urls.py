from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns=[
    path('',home,name='home'),
    #path('email',email,name='email1'),
    url('signup', signup, name='signup'),
    #path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate, name='activate')
    path('activate/(?P<uidb64>\d+)/(?P<token>\d+)/$',activate,name='activate')

]