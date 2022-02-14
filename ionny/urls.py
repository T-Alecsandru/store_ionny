from django.urls import path

from ionny import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),


]