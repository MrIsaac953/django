from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse




def contact(request):
  return render (request,'contact.html')

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



