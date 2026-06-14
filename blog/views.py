from django.shortcuts import render,get_object_or_404
from .models import Post , Category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import Http404

def blog_home (request,cat_name=None,author_username=None):   
   posts = Post.objects.filter(status=1)
   if cat_name:
      posts = posts.filter (category__name=cat_name)
   if author_username:
      posts = posts.filter(author__username__iexact=author_username ) 
   
   posts = Paginator(posts,3) 

   try:
    page_number = request.GET.get('page')
    posts = posts.get_page(page_number)
   
   except EmptyPage :
    posts = posts.get_page(posts.num_pages)
    
   

   context = {'posts':posts}
   return render (request , 'blog/blog-home.html',context)

def blog_single (request,pid):
    posts = get_object_or_404(Post,pk=pid,status = 1)
    posts.counted_view+=1
    prev_post = Post.objects.filter(pk__lt=posts.pk , status = 1).order_by('-pk').first()
    next_post = Post.objects.filter(pk__gt=posts.pk , status = 1).order_by('pk').first()
  
    context = {'posts':posts,
               'prev_post':prev_post,
               'next_post':next_post
               }
    
    posts.save()
    return render (request , 'blog/blog-single.html',context)


def blog_category(request,cat_name):
   posts = Post.objects.filter(status=1,category__name=cat_name)
   """ posts = posts.filter(category__name=cat_name) """
   context = {'posts':posts}
   return render (request , 'blog/blog-home.html',context)

def blog_search(request):
   #print(request.__dict__)
   posts = Post.objects.filter(status=1)
   if request.method == 'GET':
      #print (request.GET.get('s'))
      if s:=request.GET.get('s'):
         posts = posts.filter(content__contains = s)
    
   context = {'posts':posts}
   return render (request , 'blog/blog-home.html',context)



def test (request):
  return render (request,'test.html')