from django import template
from blog.models import Post , Category , Comment
register = template.Library()

@register.simple_tag(name='totalposts')
def function():
  posts=Post.objects.filter(status=1).count()
  return posts



@register.simple_tag(name='posts')
def function():
  posts=Post.objects.filter(status=1)
  return posts

@register.simple_tag(name='comments')
def function(pid):
  return Comment.objects.filter(post_id=pid , approved = True).count()
  

@register.filter
def snippet(value,arg):
  return value[:arg] + '...'

@register.inclusion_tag('blog/popular-posts.html')
def latestposts (arg=3):
  latest_posts=Post.objects.filter(status=1).order_by('-published_date')[:arg]
  return{'latest_posts':latest_posts}

@register.inclusion_tag('blog/category.html')
def Postcategories():
  posts = Post.objects.filter(status=1)
  categories = Category.objects.all()
  cat_dict = {}
  for name in categories:
    cat_dict[name] = posts.filter(category=name).count()
  return {'categories':cat_dict}

@register.inclusion_tag('latest_posts.html')
def latest_posts():
  posts = Post.objects.filter(status = 1).order_by('-published_date')
  return {'posts':posts}
  