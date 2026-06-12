from django.urls import path
from blog.views import *

#app_name= 'blog'

urlpatterns = [
  path('',blog_home,name = 'blog/home'),
  path('<int:pid>',blog_single, name = 'blog/single'),
  path('category/<str:cat_name>',blog_home, name = 'category') ,
  path('test/',test,name='tset')

    
]

