from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns=[
    path('',home,name='home'),
    path('signup', signup, name='signup'),
    path('activate/(?P<uidb64>\d+)/(?P<token>\d+)/$',activate,name='activate'),
    path('dashboard',dashboard,name='dashboard'),
    path('logout/(?P<name>\d+)/(?P<email>\d+)/$',user_logout,name='logout'),
    path('view',view,name='view'),
]   