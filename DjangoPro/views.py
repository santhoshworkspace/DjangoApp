from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def Home(request):
    return HttpResponse('It is home page')

def Base(request):
    return render(request,'base.html',{'title':'myapp'})

def Index(request):
    data = Post.objects.all()
    return render(request,'index.html',{'data':data})

def blog(request,idnum):
    post = get_object_or_404(Post,id=idnum)
    return render(request,'blog.html',{'post':post})