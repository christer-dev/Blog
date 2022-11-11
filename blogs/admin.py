from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'authorEmail', 'date_added', 'date_updated')
    search_fields = ('title', 'content',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

# Register your models here.
