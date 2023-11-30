from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Usuario, Participante
from .forms import FormularioInscripcion, RegistroEventoForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.contrib.auth.models import User
from django.db import IntegrityError



def pantalla_inicio(request):
    eventos = Evento.objects.all()
    return render(request, 'inicio.html', {'eventos': eventos})

def pantalla_inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            # Autentica al usuario
            usuario = authenticate(request, username=username, password=password)

            if usuario is not None:
                login(request, usuario)
                return redirect('evento')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
                return redirect('inicio_sesion')
        else:
            messages.error(request, 'Faltan campos obligatorios en la solicitud.')
            return redirect('inicio_sesion')

    return render(request, 'inicio_sesion.html')

def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')

        # Validar contraseñas coincidentes
        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'registro.html')

        try:
            # Verificar si el nombre de usuario ya existe
            if User.objects.filter(username=username).exists():
                raise ValidationError(_('El nombre de usuario ya está en uso.'), code='existing_username')

            # Obtener la fecha actual
            fecha_registro = date.today()

            # Crear el usuario
            user = User.objects.create_user(username=username, password=password)
            user.first_name = nombre
            user.last_name = apellido
            user.email = correo

            # Asignar la fecha de registro
            user.fechaRegistro_usu = fecha_registro

            user.save()

            # Autenticar al usuario y redirigir a la página de inicio
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Registro exitoso.')
            return redirect('inicio')  # Reemplaza 'nombre_de_la_pagina_de_inicio' con la URL de tu página de inicio

        except ValidationError as e:
            messages.error(request, e.message)

    return render(request, 'registro.html')




def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'evento.html', {'eventos': eventos})

@login_required
def registrar_evento(request):
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = RegistroEventoForm()
    return render(request, 'evento.html', {'form': form})




@login_required
def perfil_usuario(request):
    usuario = request.user
    participante = getattr(usuario, 'participante', None)

    context = {'usuario': usuario, 'participante': participante}
    return render(request, 'perfil_info.html', context)


@login_required
def inscribirse_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        tel_part = request.POST.get('tel_part')
        lugar_procedencia = request.POST.get('lugar_procedencia')
        fecha_llegada = request.POST.get('fecha_llegada')

        try:
            participante = Participante.objects.create(
                evento=evento,
                nombre_part=nombre,
                apellido_part=apellido,
                tel_part=tel_part,
                lugar_procedencia=lugar_procedencia,
                fecha_llegada=fecha_llegada,
                usuario=request.user,
            )
            return redirect('inicio')
        
        except IntegrityError as e:
            print(f"Error de integridad: {e}")
            pass

    return render(request, 'formulario_inscripcion.html', {'evento': evento})


