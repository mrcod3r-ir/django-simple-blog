from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
  return render(request,'blog/index.html')

def about(request):
  return render(request,'blog/about.html')

def contact(request):
  return render(request,'blog/contact.html')

def post(request):
  Posts = Post.objects.all()
  context = {
    "singlePage":True,
    "Posts":Posts
  }
  return render(request,'blog/post.html',context)

