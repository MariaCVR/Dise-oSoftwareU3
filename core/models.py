from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. EMPEZAMOS CON LAS ENUMERACIONES (No dependen de nadie)
class Estado(models.TextChoices):
    LIBRE = 'libre', 'Libre'
    OCUPADO = 'ocupado', 'Ocupado'
    MANTENIMIENTO = 'mantenimiento', 'Mantenimiento'

class Rol(models.TextChoices):
    ADMINISTRADOR = 'administrador', 'Administrador'
    CLIENTE = 'cliente', 'Cliente'

# 2. CLASES DE UBICACIÓN BÁSICA
class Direccion(models.Model):
    callePrincipal = models.CharField(max_length=100)
    calleSecundaria = models.CharField(max_length=100)
    referencia = models.CharField(max_length=200)

class Universidad(models.Model):
    nombreU = models.CharField(max_length=100)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)

class Facultad(models.Model):
    nombre = models.CharField(max_length=100)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)

class Bloque(models.Model):
    numeroBloque = models.IntegerField()
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)

# 3. CAFETERÍA Y SUS COMPONENTES
class Cafeteria(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    horaApertura = models.TimeField()
    horaCierre = models.TimeField()
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    bloque = models.ForeignKey(Bloque, on_delete=models.CASCADE)

class Menu(models.Model):
    archivo = models.FileField(upload_to='menus/')
    cafeteria = models.OneToOneField(Cafeteria, on_delete=models.CASCADE)

class Mesa(models.Model):
    codigo = models.CharField(max_length=20)
    capacidad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.LIBRE)
    cafeteria = models.ForeignKey(Cafeteria, on_delete=models.CASCADE)

# 4. USUARIO PERSONALIZADO (Combina Persona y Usuario)
class Usuario(AbstractUser):
    dni = models.CharField(max_length=15, unique=True)
    edad = models.IntegerField(null=True, blank=True)
    rol = models.CharField(max_length=20, choices=Rol.choices, default=Rol.CLIENTE)

# 5. RESERVAS Y RESEÑAS (Dependen de Usuario y Mesa)
class Reserva(models.Model):
    codigo = models.CharField(max_length=50)
    fechaReserva = models.DateTimeField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    plazoLimite = models.DateTimeField()
    numPersonas = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class MesaReserva(models.Model):
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    estado = models.CharField(max_length=20)
    fecha = models.DateTimeField()
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

class Resena(models.Model):
    calificacion = models.IntegerField()
    comentario = models.TextField()
    fechaResena = models.DateField(auto_now_add=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)