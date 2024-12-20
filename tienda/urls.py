"""
URL configuration for tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#importe para Django sirva los archivos de media (como las imágenes).
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from tienda_app import views
from tienda_app.views import mostrar_productos

#from .views import mostrar_productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro_usuario/', views.registro_usuario, name='registro_usuario' ),
    path('', views.inicio, name='inicio'),
    path('login/', views.iniciar_sesion, name='login'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('productos/', mostrar_productos, name='productos'),
    path('agregar-al-carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar-del-carrito/<int:carrito_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('procesar-compra/', views.procesar_compra, name='procesar_compra'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para mostrar img
