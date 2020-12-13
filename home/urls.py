from django.urls import path, include

from . import views

urlpatterns = [
    path('enterphone/', views.Modal, name = 'modal'), 
    path('home/', views.Home, name = 'home'),
    path('safety/', views.Safety, name = 'safety'),
    path('contact/', views.Contact, name = 'contact'),
    path('help/', views.Help, name = 'help'),
    path('message/', views.Message, name = 'message'),
    path('photo/', views.Photo, name = 'photo'),
    path('audio/', views.Audio, name = 'audio'),
   
]