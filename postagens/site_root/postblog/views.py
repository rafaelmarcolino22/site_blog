from django.shortcuts import render
from . models import Post

def Index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})    

# Create your views here.
