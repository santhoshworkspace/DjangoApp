from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='Login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/login/'),name='logout')
]
