
from django.test import TestCase
from .models import Evento

class EventoModelTest(TestCase):
    def test_evento_model(self):
        evento = Evento(nombre="Evento de prueba", fecha="2023-01-01", descripcion="Descripción de prueba")
        self.assertEqual(str(evento), evento.nombre)

