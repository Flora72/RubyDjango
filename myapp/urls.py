from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='my_index'),
    path('about', views.about, name='my_about'),
    path('contact/', views.contact, name='my_contact'),
    path('blogs', views.blogs, name='my_blogs'),
    path('services', views.services, name='my_services')
]
