from django.urls import path
from website.views import *
""" from website.feeds import RssContactFeeds """

app_name = 'website'

urlpatterns = [
    path ('contact',contact , name = 'contact'),
    path ('about',about , name= 'about'),
    path ('json',json),
    path('',index),
    path('elements',elements , name= 'elements'),
    path('index',index , name = 'index'),
    path('test',test_view , name ='test'),
    path('newsletter',newsletter,name='newsletter'),
  

]
