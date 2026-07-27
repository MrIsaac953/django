from django.contrib import admin
from .models import Post , Category , Comment
from django_summernote.admin import SummernoteModelAdmin



#@admin.register(Post)  decorator
class PostAdmin (SummernoteModelAdmin):
  date_hierarchy = "created_date"
  #empty_value_display = "-empty-"
  #fields = ["title",'content']
  list_display = ['title','author','counted_view','login_require','status','published_date','created_date','updated_date']
  list_filter = ['status','author']
  #ordering = ['updated_date']
  #search_fields = ['title','content']
  summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin (admin.ModelAdmin):
  list_display = ['name','post','approved','created_date']
  list_filter = ['post','approved']
  date_hierarchy = "created_date"
  ordering = ['-created_date']


admin.site.register(Post,PostAdmin)
admin.site.register(Category)

