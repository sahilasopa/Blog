from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class BlogUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=52)
    username = models.CharField(unique=True, max_length=15)
    email = models.EmailField(blank=True, unique=True)

    def get_absolute_url(self):
        return f'/profile/{self.id}'

    def __str__(self):
        return self.full_name


class Blog(models.Model):
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    blog = RichTextField()
    image = models.ImageField(blank=True, null=True, upload_to='media')
    uploaded_on = models.DateTimeField(auto_now=True)
    views = models.ManyToManyField(BlogUser, blank=True, related_name='Views')
    likes = models.ManyToManyField(BlogUser, blank=True, related_name='Likes')
    comments = models.CharField(blank=True, max_length=120)

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return f"/post/{self.id}/"


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    contact_no = models.CharField(max_length=12, blank=True)
    message = models.TextField()
