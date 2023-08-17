from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blogpage'),
    path('contact',views.contact,name='contact'),
    path('search',views.search,name='search'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('logoutfn',views.logoutuserfn,name='logoutfn'),
    path('signup',views.signupuser,name='signup'),
]

