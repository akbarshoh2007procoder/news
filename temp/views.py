from django.http import request
from django.shortcuts import render
from .models import Blog, Tags 



def main(requests):
    blog = Blog.objects.order_by("-create_at")[:5]
    tags = Tags.objects.all()
   
    return render(requests,"index.html",{'blogs':blog,'tag':tags})
    

def blog(requests):
    return render(requests,"blog.html")

def contact(requests):
    return render(requests,"Contact_us.html")

def single(requests):
    return render(requests,"single.html")
