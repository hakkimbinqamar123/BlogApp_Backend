from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('addblog/',views.addBlog,name='addblog'),
    path('viewblog/',views.view_blog,name='viewblog'),
    path('mypost/',views.ViewMypost,name='mypost'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('myprofile/',views.ViewMyprofile,name='myprofile'),
]