
from django.contrib import admin
from .models import Post
# Register your models here.
from django.utils.safestring import mark_safe

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','photo_tag','message','is_public', 'message_length','created_at','updated_at']
    list_display_links = ['message']
    list_filter = ['created_at']
    search_fields = ['message']
    def photo_tag(self,post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:83px;"/>')
        return None
    def message_length(self,post):
        return len(post.message)
    message_length.short_description = "메세지 글자수"