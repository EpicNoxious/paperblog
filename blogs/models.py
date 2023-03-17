from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from datetime import datetime, date
import uuid 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to='images/', default="images/default.jpeg")
    date_of_create = models.DateField(auto_now_add=True)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name="blog_post")
    
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog', args=[str(self.id)])

    @property 
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

