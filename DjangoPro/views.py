from django.shortcuts import render
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