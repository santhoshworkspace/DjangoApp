from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='blog-home'),
    path('index',views.Index,name="Index"),
    path('base',views.Base,name='basecode'),
    path('blog/<str:slug>/',views.blog,name='blogs')
]
