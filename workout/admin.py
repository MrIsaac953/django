from django.contrib import admin
from .models import mine

class mineAdmin(admin.ModelAdmin):
  list_display=['title','created_date','published_date','updated_date']
 


admin.site.register(mine,mineAdmin)


# Register your models here.
