from django.contrib import admin
from .models import contact

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
  date_hierarchy = 'created_date'
  list_display = ['name','subject','email','created_date']
  list_filter = ['email']
  search_fields = ['subject','message']




# Register your models here.
