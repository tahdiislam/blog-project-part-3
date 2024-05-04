from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    categories = models.ManyToManyField(Category) # one post can have multiple category and one category have multiple post
    author = models.ForeignKey(User, on_delete=models.CASCADE) # post will be automatically delete if author is deleted
    def __str__(self) -> str:
        return f"Title: {self.title}"