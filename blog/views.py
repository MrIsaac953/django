from django.shortcuts import render,get_object_or_404 ,redirect
from .models import Post , Category , Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import Http404
from taggit.models import Tag
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def blog_home (request,cat_name=None,author_username=None,tag_name=None):   
   posts = Post.objects.filter(status=1)
   tags = Tag.objects.filter(post__in=posts).distinct()
   
   
   if cat_name:
      posts = posts.filter (category__name=cat_name)
   if author_username:
      posts = posts.filter(author__username__iexact=author_username ) 
   if tag_name:
      posts = posts.filter(tags__name__in=[tag_name] ) 
   
   posts = Paginator(posts,3) 

   try:
    page_number = request.GET.get('page')
    posts = posts.get_page(page_number)
   
   except EmptyPage :
    posts = posts.get_page(posts.num_pages)
    
   

   context = {'posts':posts,
              'tags':tags,
              }
   return render (request , 'blog/blog-home.html',context)
""" @login_required """
def blog_single (request,pid):
   if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
         form.save()
         messages.add_message(request, messages.SUCCESS, "Your message submited , Thank You.")
      else:
          messages.add_message(request,messages.ERROR , "Your message not submited , try again")
               
    
   posts = get_object_or_404(Post,pk=pid,status = 1)
   posts.counted_view+=1
    
   prev_post = Post.objects.filter(pk__lt=posts.pk , status = 1).order_by('-pk').first()
   next_post = Post.objects.filter(pk__gt=posts.pk , status = 1).order_by('pk').first()
   posts.save()  
   
   if posts.login_require and not request.user.is_authenticated:
      """login_url = reverse('accounts:login')"""   # برو به صفحه لاگین ولی یادت باشه کاربر از کجا اومده
      return redirect(f'/accounts/login/?next={request.path}')
   
   comments = Comment.objects.filter(post=posts.id , approved = True)
   form = CommentForm()   
   context = {'posts':posts,
            'prev_post':prev_post,
            'next_post':next_post,
            'comments' : comments,
            'form':form,
            }  
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

