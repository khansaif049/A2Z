from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='main'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("projects",views.projects,name='projects'),
    
    path("plan",views.plan,name='plan'),

    path("single",views.single,name='single'),
    path("contacts",views.contacts,name='contacts'),
    path("payme",views.payme,name='payme'),
    path("suce",views.suce,name='suce'),

]