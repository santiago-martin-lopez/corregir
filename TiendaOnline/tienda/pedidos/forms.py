from django import forms


class Formucliente(forms.Form):
    nombre_cliente=forms.CharField(max_length=100)
    email_cliente=forms.EmailField()
    telefono_cliente=forms.IntegerField()
    direccion_cliente=forms.CharField(max_length=100)

class Formuarticulo(forms.Form):
    nombre=forms.CharField(max_length=100)
    categoria=forms.CharField(max_length=100)
    precio=forms.IntegerField()

class Formupedidos(forms.Form):
    fecha=forms.DateField()
    entrega=forms.BooleanField()
    codigo_seguimiento=forms.CharField(max_length=100)