import sys
import os

# Agregar la ruta de la carpeta 'app' al path para que Python pueda importar 'mi_clase'
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.tarea import Tarea
import unittest

class TestTarea(unittest.TestCase):

    def test_setters_and_getters(self):
        tarea = Tarea("Tarea 1", "Descripción de la tarea", "2023-08-31")

        tarea.nombre = "Nueva Tarea"
        self.assertEqual(tarea.nombre, "Nueva Tarea")

        tarea.descripcion = "Nueva descripción"
        self.assertEqual(tarea.descripcion, "Nueva descripción")

        tarea.fecha_vencimiento = "2023-09-15"
        self.assertEqual(tarea.fecha_vencimiento, "2023-09-15")

if __name__ == '__main__':
    unittest.main()