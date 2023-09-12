from django.contrib import admin
from django.urls import include, path
from blogs import views

urlpatterns = [
    path('sheela',views.blog_home,name='homepage'),
    path('editor',views.posts,name='posts'),
    path('logout',views.logout,name='logout'),
]