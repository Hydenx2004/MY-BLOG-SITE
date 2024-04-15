from django.db import models

# Create your models here.

class Blog(models.Model):

    Author = models.CharField(max_length=128)
    Blog_Id =models.IntegerField(unique=True)
    Title = models.CharField(max_length=128)
    Content = models.TextField()
    Date = models.DateTimeField(auto_now=True)
    Image = models.ImageField(upload_to='Pictures/%Y/%m/%d',blank=True,null=True,max_length=255)

class Blog_id(models.Model):

    Blog_Id =models.IntegerField()


