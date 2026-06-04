from django.db import models

class mine (models.Model) :
  title = models.CharField(max_length=255)
  content = models.TextField()
  published_date = models.DateTimeField(null=1)
  created_date = models.DateTimeField(auto_now_add=1)
  updated_date = models.DateTimeField(auto_now=1)
  counted_view = models.IntegerField(default=0)

  class Meta:
     verbose_name_plural = 'for mine workouts'
     #abstract = True
     ordering=['-published_date']
     
    
  def __str__(self):
      return self.title
""" 
class all (mine):
   status = models.BooleanField(default=False) """
      