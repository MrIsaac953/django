from django.shortcuts import render , redirect
from django.http import JsonResponse
from django.http import HttpResponse ,HttpResponseRedirect
from website.models import  Contact
from .forms import NameForm,ContactForm,NewletterForm 
from django.contrib import messages




def contact(request):
  if request.method =="POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      """ contact = form.save(commit=False)
      contact.name='unknown' """
      form.save()
      messages.add_message(request, messages.SUCCESS, "Your information submited , Thank You.")
    else:
      messages.add_message(request,messages.ERROR , "Your Information is wrong")
  form  = ContactForm()
  return render (request,'contact.html',{'form':form})

def json (request):
  return JsonResponse ({'info':{'name':'Farhan',
                        'age' : 22,
                        'lname' : "Isaacnia",
                        'job' :['computer engineer' , 'sdfsdf'],
                        'address':{
                          'city':'Tehran'
                        }}}) 

def about(request):
  return render (request,'about.html')

def index (request):
  return render (request,'index.html')

def elements (request):
  return render (request , 'elements.html')


def newsletter(request):
  if request.method=='POST':
    form = NewletterForm(request.POST)
    if form.is_valid:
      form.save()
      messages.add_message(request, messages.SUCCESS, "Your Email submited , Thank You.")
    else:
      messages.add_message(request,messages.ERROR , "Your Email is wrong")
  return redirect(request.POST.get('next','/'))
  


def test_view (request):
  if request.method == 'POST':
   form = ContactForm(request.POST)
   
   if form.is_valid():
     
     form.save()
     """ name = form.cleaned_data["name"]
     email = form.cleaned_data["email"]
     subject = form.cleaned_data["subject"]
     message = form.cleaned_data["message"]
     print(name,email,subject,message) """
     return HttpResponse ('done')
   else :
     return HttpResponse ('not valid')
  
  form = ContactForm()
  return render (request , 'test.html',{'form':form})



