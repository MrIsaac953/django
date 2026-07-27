from django.contrib import admin
from .models import  Contact , Newsletter

@admin.register( Contact)
class contactAdmin(admin.ModelAdmin):
  date_hierarchy = 'created_date'
  list_display = ['name','subject','email','created_date']
  list_filter = ['email']
  """ search_fields = ['subject','message'] """

admin.site.register(Newsletter)

# Register your models here.
