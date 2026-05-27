from django.urls import path
from website.views import *

urlpatterns = [
    path ('home',home),
    path ('about',about),
    path ('json',json),
    path('',index)
]
