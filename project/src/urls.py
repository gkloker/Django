from django.conf.urls import url
from src import views

urlpatterns = [
    url('home', views.home, name="Home"),
    url('servicios', views.services, name="Services"),
    url('tienda', views.store, name="Store"),
    url('blog', views.blog, name="Blog"),
    url('contacto', views.contact, name="Contact"),
]