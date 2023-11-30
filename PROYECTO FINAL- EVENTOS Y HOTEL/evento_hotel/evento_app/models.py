

from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission, User

class Usuario(AbstractUser):
    Id_usuario = models.BigAutoField(primary_key=True)
    nombre_usu = models.CharField(max_length=20)
    apellido_usu = models.CharField(max_length=30)
    correo_usu = models.EmailField(max_length=45)
    fechaRegistro_usu = models.DateField(auto_now_add=True)
    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios')

class Empleado(models.Model):
    Id_empleado = models.BigAutoField(primary_key=True)
    nombre_emple = models.CharField(max_length=30)
    apellido_emple = models.CharField(max_length=30)
    telef_emple = models.BigIntegerField()
    correo_emple = models.EmailField(max_length=45)
   

class Evento(models.Model):
    nombre_evento = models.CharField(max_length=30)
    fecha_evento = models.DateField()
    lugar_evento = models.CharField(max_length=30)
    descripcion_evento = models.CharField(max_length=100)
    presupuesto_evento = models.BigIntegerField()
    id = models.BigAutoField(primary_key=True)

class EventoEmpleado(models.Model):
    ID_EMPLEADO = models.BigIntegerField()
    ID_EVENTO = models.BigIntegerField()
    fecha_asignacion = models.DateField()
    horario_de_trabajo = models.TimeField()

class Agenda(models.Model):
    Id_evento = models.BigIntegerField()
    fecha_event_agend = models.DateField()
    hora_event_agend = models.TimeField()
    lugar_event_agend = models.CharField(max_length=30)


class Acompanante(models.Model):
    nombre_acomp = models.CharField(max_length=20)
    apellido_acomp = models.CharField(max_length=20)
    dni_acomp = models.BigIntegerField()
    tel_acomp = models.BigIntegerField()
    Id_part = models.BigIntegerField()

class Participante(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='participantes')
    nombre_part = models.CharField(max_length=20)
    apellido_part = models.CharField(max_length=20)
    tel_part = models.BigIntegerField()
    lugar_procedencia = models.CharField(max_length=30)
    fecha_llegada = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_part} {self.apellido_part} - Evento: {self.evento}"

    class Meta:
        verbose_name_plural = "Participantes"