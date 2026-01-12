from django.contrib import admin
from .models import (Direccion, Universidad, Facultad, Bloque, 
                     Cafeteria, Menu, Mesa, Usuario, Reserva, 
                     MesaReserva, Resena)

# Esto hace que las tablas aparezcan en el panel
admin.site.register(Direccion)
admin.site.register(Universidad)
admin.site.register(Facultad)
admin.site.register(Bloque)
admin.site.register(Cafeteria)
admin.site.register(Menu)
admin.site.register(Mesa)
admin.site.register(Usuario)
admin.site.register(Reserva)
admin.site.register(MesaReserva)
admin.site.register(Resena)