from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from tienda_app.models import Producto
from .models import Producto, Carrito# Pylint: disable=no-member
from .forms import UsuarioForm
from .forms import ContactForm
from .models import Carrito






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

def cerrar_sesion(request):
    logout(request)  # Esto cierra la sesión del usuario
    return redirect('inicio')



def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto.html', {'productos':productos})

@login_required
def agregar_al_carrito(request, producto_id):

    if not request.user.is_authenticated:
        return redirect('login')
    producto = Producto.objects.get(id=producto_id)
    carrito, created = Carrito.objects.get_or_create(user=request.user, producto=producto)

    if not created:
        carrito.cantidad += 1
        carrito.save()

    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito_items = Carrito.objects.filter(user=request.user)
    total = sum(item.total for item in carrito_items)
    return render(request, 'carrito.html', {'carrito_items': carrito_items, 'total': total})

@login_required
def eliminar_del_carrito(request, carrito_id):
    carrito_item = Carrito.objects.get(id=carrito_id)
    carrito_item.delete()
    return redirect('ver_carrito')

def contacto_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Lógica para procesar el formulario, como enviar un correo o guardar datos

            # Mostrar mensaje de éxito
            messages.success(request, "Formulario enviado con éxito. ¡Gracias por contactarnos!")

            # Limpiar el formulario
            form = ContactForm()
        else:
            messages.error(request, "Hubo un error en el formulario. Por favor, revisa los campos.")
    else:
        form = ContactForm()

    return render(request, 'contacto.html', {'form': form})


"""@login_required
def procesar_compra(request):
    # carrito_items = Carrito.objects.filter(user=request.user)
    carrito = Carrito.objects.filter(user=request.user).first()
    if carrito is None:
        return render(request, 'error.html', {'mensaje': 'No tienes un carrito activo.'})

    carrito_items = carrito.carritoproducto_set.all()

# para simular la compra
    if request.method == "POST":
        # limpiar el carrito
        carrito.carritoproducto_set.all().delete()
        return render(request, 'finalizada.html')

    context = {
        'carrito_items': carrito_items,
        'total': sum(item.producto.precio * item.cantidad for item in carrito_items)
    }
    return render(request, 'compra.html', context)"""


@login_required
def procesar_compra(request):
    carrito_items = Carrito.objects.filter(user=request.user)

    if not carrito_items.exists():
        return render(request, 'error.html', {'mensaje': 'No tienes productos en tu carrito.'})

    if request.method == "POST":
        carrito_items.delete()
        return render(request, 'finalizada.html')

    # Añadir el subtotal a cada item del carrito
    for item in carrito_items:
        item.subtotal = item.total  # Usa la propiedad `total` del modelo

    total = sum(item.total for item in carrito_items)

    context = {
        'carrito_items': carrito_items,
        'total': total,
    }
    return render(request, 'compra.html', context)




# Create your views here.
