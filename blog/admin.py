from django.contrib import admin
from blog.models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
   list_display = ['title','created_time','modified_time','category','author']



# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
