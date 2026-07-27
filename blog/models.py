from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils.text import slugify


class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Post (models.Model):
  author= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  image= models.ImageField(upload_to='blog/',default= 'blog/default.jpg')
  title = models.CharField(max_length=255)
  content = models.TextField()
  category = models.ManyToManyField(Category)
  tags = TaggableManager()
  counted_view = models.IntegerField(default = 0)
  login_require = models.BooleanField(default=False)
  status = models.BooleanField(default=False)
  published_date = models.DateTimeField(null=True)
  created_date = models.DateTimeField(auto_now_add=True) 
  updated_date = models.DateTimeField(auto_now=True) 
 


  class Meta :
    ordering =['-created_date']
    #verbose_name = 'خر بابا بزرگ'
    #verbose_name_plural = 'خر های بابا بزرگ'

  def __str__(self):
    return self.title
  
  def get_absolute_url (self):
    return reverse ('blog/single',kwargs={'pid':self.id}) #args = [self.id]
  
 
class Comment(models.Model):
  post = models.ForeignKey(Post,on_delete=models.CASCADE)
  name = models.CharField()
  email = models.EmailField()
  subject = models.CharField()
  message = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)
  approved = models.BooleanField(default=False)

  class Meta:
    ordering = ['-created_date']
  def __str__(self):
    return self.name

  
  