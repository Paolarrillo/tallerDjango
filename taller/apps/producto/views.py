# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import producto, categoria
from django.views.generic import ListView
from .forms import *

def index(request):
	return HttpResponse("Esta es la respuesta")

def plantilla(request):
	return render(request, 'producto/index.html')

# def categorias(request):
# 	contexto = {
# 		'categorias': categoria.objects.all()
# 	}
# 	return render(request, 'producto/categorias.html', contexto)

def productos(request):
    contexto = {
    	'productos': producto.objects.all()
    }
    return render(request, 'producto/productos.html', contexto)

class viewCategorias(ListView):
	model = categoria
	template_name = 'producto/categorias.html'
	queryset = categoria.objects.all()

def nuevoRegistro(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('producto:productos')
	else:
		form = ProductoForm()
	return render(request, 'producto/productoFormulario.html', {'form' : form})

def editarRegistro(request, idProducto):
	productoid = producto.objects.get(id=idProducto)
	if request.method == 'GET':
		form = ProductoForm(instance = productoid)
	else:
		form = ProductoForm(request.POST, instance=productoid)
		if form.is_valid():
			form.save()
		return redirect('producto:productos')
	return render(request, 'producto/productoFormulario.html', {'form' : form})
def eliminarRegistro(request, idProducto):
	productoid = producto.objects.get(id=idProducto).delete()
	return redirect('producto:productos')

def nuevaCategoria(request):
	print (request.POST)
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('producto:categorias')
	else:
		form = CategoriaForm()
	return render(request, 'producto/categoriaFormulario.html', {'form' : form})

def editarCategoria(request, idCategoria):
	categoriaid = categoria.objects.get(id=idCategoria)
	if request.method == 'GET':
		form = CategoriaForm(instance = categoriaid)
	else:
		form = CategoriaForm(request.POST, instance=categoriaid)
		if form.is_valid():
			form.save()
		return redirect('producto:categorias')
	return render(request, 'producto/categoriaFormulario.html', {'form' : form})

def eliminarCategoria(request, idCategoria):
	categoriaid = categoria.objects.get(id=idCategoria).delete()
	return render(request, 'producto/categorias.html')

def comprar(request, id):
   producto = productos.objects.get(id = id)

    context = {
            'producto': producto
    }

    if(request.method == "POST"):
        cantidad = request.POST.get('qty')
        if(int(cantidad) > int(producto.quantity) or int(cantidad) <= 0):
            return error(request)
        else:
            producto.quantity -= int(cantidad)
            producto.save()
            return render(request, 'productos/comprar.html', context)

    return render(request, 'productos/comprar.html', context)