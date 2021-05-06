from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.home,name='home'),
    path("main",views.index,name='main'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("projects",views.projects,name='projects'),
    
    path("plan",views.plan,name='plan'),

    path("single",views.single,name='single'),
    path("contacts",views.contacts,name='contacts'),
    path("payme",views.payme,name='payme'),
    path("suce",views.suce,name='suce'),
    path("login1",views.login1,name="login1"),
    path("regi",views.regi,name="regi"),
    path("logout",views.logout,name="logout"),
    

]