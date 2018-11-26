from django import forms
from .models import producto, categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = [
        'nombre',
        'f_creacion'
        ]
        labels = {
        'nombre' : 'nombre',
        'f_creacion' : 'f_creacion',
        }
        widgets = {
        'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
        'f_creacion' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = [
        'nombreProducto',
        'descripcion',
        'costo',
        'disponible',
        'n_existencias',
        'categoria',
        ]
        labels = {
        'nombreProducto' : 'Producto',
        'descripcion' : 'descripcion',
        'costo' : 'costo',
        'disponible' : 'disponible',
        'n_existencias' : 'existencias',
        'categoria' : 'categoria',
        }
        widgets = {
        'Producto' : forms.TextInput(attrs={'class' : 'form-control'}),
        'descripcion' : forms.TextInput(attrs={'class' : 'form-control'}),
        'costo' : forms.TextInput(attrs={'class' : 'form-control'}),
        'disponible' : forms.TextInput(attrs={'class' : 'form-control'}),
        'producto' : forms.TextInput(attrs={'class' : 'form-control'}),
        'existencias' : forms.TextInput(attrs={'class' : 'form-control'}),
        'categoria' : forms.TextInput(attrs={'class' : 'form-control'}),
        }
