from django.shortcuts import render, get_object_or_404
from . models import Post

def Index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})    

def MateriaPost(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'materia.html', {'post':post})
# Create your views here.
