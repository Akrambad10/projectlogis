from django.contrib import admin
from django.urls import path
from logisapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),

]
