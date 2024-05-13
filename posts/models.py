from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    categories = models.ManyToManyField(Category) # one post can have multiple category and one category have multiple post
    author = models.ForeignKey(User, on_delete=models.CASCADE) # post will be automatically delete if author is deleted
    image = models.ImageField(upload_to='posts/media/uploads/', null=True, blank=True)
    def __str__(self) -> str:
        return f"Title: {self.title}"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"Comments by {self.name}"
    