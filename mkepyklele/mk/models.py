from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100)
    slug = models.SlugField(default=True)
    published = models.BooleanField(default=True)

    class Meta: 
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    class Meta: 
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    class Meta: 
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

class NewsletterUser(models.Model):
    user_email = models.EmailField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_email
