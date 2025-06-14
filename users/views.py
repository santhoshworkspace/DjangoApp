from django.shortcuts import render,redirect
from .forms import CustomUserCreationFrom
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
       form =CustomUserCreationFrom(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request,f'Account created for {username}!')
           return redirect('Index')
    else:
        form =CustomUserCreationFrom()
    return render(request,'register.html',{'form':form})