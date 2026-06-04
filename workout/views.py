from django.shortcuts import render ,get_object_or_404
from .models import mine
from django.utils import timezone
def workout(request):
  post = mine.objects.filter(published_date__lte=timezone.now())
  context = {'posts':post}
  return render (request,'workout/workout.html',context)

def workout_view (request,pk):
  post = get_object_or_404(mine,pk=pk)
  post.counted_view+=1
  #contex={'posts':post}
  post.save()
  return render (request,'workout/workout_view.html',{'posts':post})
