import datetime
from unittest import TestCase
from unittest.mock import Mock

from app.lista_de_tareas import ListaDeTareas
from app.tarea import Tarea


class TestListaDeTareas(TestCase):
    def setUp(self):
        self.mock_tarea1 = Mock(spec=Tarea, nombre="Tarea 1", descripcion="Descripcion 1",
                                fecha_vencimiento=datetime.datetime(2023, 1, 1), estado=False)
        self.mock_tarea2 = Mock(spec=Tarea, nombre="Tarea 2", descripcion="Descripcion 2",
                                fecha_vencimiento=None, estado=False)
        self.mock_tarea3 = Mock(spec=Tarea, nombre="Tarea 3", descripcion="Descripcion 3",
                                fecha_vencimiento=datetime.datetime(2023, 12, 31), estado=False)
        self.lista = ListaDeTareas("lista1")

    def aprovisionar_lista(self):
        self.lista.agregar_tarea_nueva(self.mock_tarea1)
        self.lista.agregar_tarea_nueva(self.mock_tarea2)
        self.lista.agregar_tarea_nueva(self.mock_tarea3)

    def test_agregar_tarea_nueva(self):
        self.assertEqual(len(self.lista.tareas), 0)

        self.lista.agregar_tarea_nueva(self.mock_tarea1)
        self.assertEqual(len(self.lista.tareas), 1)

        self.lista.agregar_tarea_nueva(self.mock_tarea2)
        self.lista.agregar_tarea_nueva(self.mock_tarea3)
        self.assertEqual(len(self.lista.tareas), 3)

    def test_eliminar_tarea(self):
        self.aprovisionar_lista()

        self.lista.eliminar_tarea(2)
        self.assertEqual(len(self.lista.tareas), 2)

    def test_modificar_tarea_nombre(self):
        self.lista.agregar_tarea_nueva(self.mock_tarea1)

        nuevo_nombre = "tarea001"
        self.lista.modificar_tarea_nombre(0, nuevo_nombre)
        self.assertEqual(self.lista.tareas[0].nombre, nuevo_nombre)

    def test_modificar_tarea_descripcion(self):
        self.lista.agregar_tarea_nueva(self.mock_tarea1)

        nuevo_nombre = "tarea001"
        self.lista.modificar_tarea_nombre(0, nuevo_nombre)
        self.assertEqual(self.lista.tareas[0].nombre, nuevo_nombre)

    def test_agregar_o_modificar_tarea_fecha_vencimiento(self):
        self.lista.agregar_tarea_nueva(self.mock_tarea1)
        self.lista.agregar_tarea_nueva(self.mock_tarea2)
        nueva_fecha = datetime.datetime(1990, 12, 31)

        self.lista.agregar_o_modificar_tarea_fecha_vencimiento(0, nueva_fecha)
        self.assertEqual(self.lista.tareas[0].fecha_vencimiento, nueva_fecha)

        self.lista.agregar_o_modificar_tarea_fecha_vencimiento(1, nueva_fecha)
        self.assertEqual(self.lista.tareas[1].fecha_vencimiento, nueva_fecha)

    def test_eliminar_tarea_fecha_vencimiento(self):
        self.lista.agregar_tarea_nueva(self.mock_tarea1)

        self.lista.eliminar_tarea_fecha_vencimiento(0)
        self.assertIsNone(self.lista.tareas[0].fecha_vencimiento)

    def test_cambiar_estado_tarea(self):
        self.mock_tarea1.cambiar_estado.side_effect = lambda: setattr(self.mock_tarea1, "estado",
                                                                      not self.mock_tarea1.estado)
        self.lista.agregar_tarea_nueva(self.mock_tarea1)

        self.assertFalse(self.lista.tareas[0].estado)
        self.lista.cambiar_estado_tarea(0)
        self.assertTrue(self.lista.tareas[0].estado)
