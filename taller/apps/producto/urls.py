from django.conf.urls import url
from .views import index, plantilla, productos, viewCategorias, nuevoRegistro, editarRegistro, eliminarRegistro, nuevaCategoria, editarCategoria, eliminarCategoria

app_name = 'productos'
urlpatterns=[
    url(r'^index/$', index),
    url(r'^plantilla/$', plantilla),
    url(r'^categorias/$', viewCategorias.as_view(), name='categorias'),
    url(r'^productos/$', productos, name='productos'),
    url(r'^productos/nuevoRegistro/$', nuevoRegistro, name='nuevoRegistro'),
    url(r'^productos/editarRegistro/(?P<idProducto>\d+)$', editarRegistro, name='editarRegistro'),
    url(r'^productos/eliminarRegistro/(?P<idProducto>\d+)$', eliminarRegistro, name='eliminarRegistro'),
    url(r'^categorias/nuevaCategoria/$', nuevaCategoria, name='nuevaCategoria'),
    url(r'^categorias/editarCategoria/(?P<idCategoria>\d+)$', editarCategoria, name='editarCategoria'),
    url(r'^categorias/eliminarCategoria/(?P<idCategoria>\d+)$', eliminarCategoria, name='eliminarCategoria'),
]
