from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title       = models.CharField(max_length = 120)
    description = models.TextField()
    image       = models.ImageField(upload_to='blog/%Y/%m/%d/')
    created     = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title


class Contact(models.Model):
    name    = models.CharField(max_length = 130)
    email   = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Picture(models.Model):
    author   = models.OneToOneField(User, on_delete= models.CASCADE)
    chef     = models.ImageField(upload_to='user/%Y/%m/%d/')
    logo     = models.ImageField(upload_to='logo/%Y/%m/%d/', blank = True)
    header   = models.ImageField(upload_to='headers/%Y/%m/%d/')
    uploaded = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.uploaded