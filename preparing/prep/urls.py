from django.urls import path
from prep import views

urlpatterns = [
    path("",views.register,name='register'),
    path("login/",views.login_up,name='login'),
    path("home/",views.home,name='home'),
    
    ]
