
from django.db import models

# Create your models here.

class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank =True,upload_to='instagram/post/%Y%m%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        # return f"cu stom Post objects({self.id})"
        return self.message
    
    class Meta:
        ordering =['-id']
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description ="메세지 글자수"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)