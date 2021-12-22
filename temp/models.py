
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Tags(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    
class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tags)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    photo = models.ImageField(upload_to="static/photos")
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title