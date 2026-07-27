from django.urls import path
from blog.views import *
from blog.feeds import RssPostsFeeds

#app_name= 'blog'

urlpatterns = [
  path('',blog_home,name = 'blog/home'),
  path('<int:pid>',blog_single, name = 'blog/single'),
  path('category/<str:cat_name>',blog_home, name = 'category') ,
  path('tags/<str:tag_name>',blog_home, name = 'tags') ,
  path('author/<str:author_username>/', blog_home , name = 'author'),
  path('search/',blog_search,name='search'),
  path('test/',test,name='tset'),
  path("posts/rss/", RssPostsFeeds(), name="posts_feed"),

    
]

