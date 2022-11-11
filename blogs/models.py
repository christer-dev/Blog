from django.db import models
from users.models import CustomUser, Profile
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    authorEmail = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    picture = models.ImageField(blank=True, null=True,default='defaultBlogPic.jpg', upload_to='blog_images')
    likes = models.ManyToManyField(CustomUser, related_name="blog_post")

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['date_added']