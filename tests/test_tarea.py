import datetime
from unittest import TestCase

from app.tarea import Tarea


class TestTarea(TestCase):
    def setUp(self):
        self.fecha_vencimiento = datetime.datetime(2023, 12, 31, 23, 59, 59)
        self.tarea = Tarea("tarea1", "descripcion 1", self.fecha_vencimiento)

    def test_cambiar_estado(self):
        # El estado inicial debe ser falso
        self.assertFalse(self.tarea.estado)

        # Cambiar estado
        self.tarea.cambiar_estado()
        self.assertTrue(self.tarea.estado)

        # Cambiar estado de nuevo
        self.tarea.cambiar_estado()
        self.assertFalse(self.tarea.estado)
