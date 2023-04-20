from django.urls import path
from .views import *



urlpatterns=[

 path('userregister/', userregister.as_view(), name='userregister'),
 path('userlogin/', userlogin.as_view(), name='userlogin'),
 path('index/',index),
 path('home/', home),
 path("bookupload/",bookupload.as_view(), name='bookupload'),
 path("bookdelete/<pk>",bookdelete.as_view(), name='bookdelete'),
 path("bookupdate/<pk>",bookedit.as_view(), name='bookupdate'),
 path("bookdownload/",bookdownloads.as_view(), name='bookdownload'),
 path("booklogout/",bookllogoutview.as_view(), name='booklogout'),








]



