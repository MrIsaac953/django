from django.contrib import admin
from .models import Post


#@admin.register(Post)  decorator
class PostAdmin (admin.ModelAdmin):
  date_hierarchy = "created_date"
  #empty_value_display = "-empty-"
  #fields = ["title",'content']
  list_display = ['title','content','counted_view','status','published_date','created_date','updated_date']
  list_filter = ['status']
  #ordering = ['updated_date']
  search_fields = ['title','content']
admin.site.register(Post,PostAdmin)

