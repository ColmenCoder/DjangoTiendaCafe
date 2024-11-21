from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
#from tienda_app.models import Producto
from .models import Producto # Pylint: disable=no-member
from .forms import UsuarioForm






def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión')
            return redirect('login')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
            return render(request, 'registro.html', {'form': form})
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})



def inicio(request):
    return render(request, 'inicio.html' )


def iniciar_sesion(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        return render(request, 'login.html', {'error': '= "Los datos son incorrectos. Por favor, inténtalo de nuevo.'})
    return render (request, 'login.html')



def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto.html', {'productos':productos})








# Create your views here.
