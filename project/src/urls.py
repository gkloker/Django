from django.conf.urls import url
from src import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('home', views.home, name="Home"),
    url('tienda', views.store, name="Store"),
    url('contacto', views.contact, name="Contact"),
]

# permite visualizar la imagen que cargamos desde el panel de administracion

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)