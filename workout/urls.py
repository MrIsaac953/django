from django.urls import path
from .views import *

urlpatterns = [
    path('',workout,name='workout'),
    path('<int:pk>/',workout_view,name='view')
]
