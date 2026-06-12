from django.shortcuts import render,get_object_or_404
from .models import Post , Category

def blog_home (request,cat_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter (category__name=cat_name)
    context = {'posts':posts}
    return render (request , 'blog/blog-home.html',context)

def blog_single (request,pid):
    posts = get_object_or_404(Post,pk=pid,status = 1)
    posts.counted_view+=1
    context = {'posts':posts}
    posts.save()
    return render (request , 'blog/blog-single.html',context)


def blog_category(request,cat_name):
   posts = Post.objects.filter(status=1,category__name=cat_name)
   """ posts = posts.filter(category__name=cat_name) """
   context = {'posts':posts}
   return render (request , 'blog/blog-home.html',context)



def test (request):
  return render (request,'test.html')