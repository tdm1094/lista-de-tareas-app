# Imports
import datetime
from tarea import Tarea

class ListaDeTareas:

    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregarTareaNueva(self, nombre, descripcion, fecha_vencimiento):
        tarea = Tarea(nombre, descripcion, fecha_vencimiento)
        self.tareas.append(tarea)

    def eliminarTarea(self, tarea):
        self.tareas.remove(tarea)

    def modificarNombreTarea(self, tarea, nuevo_nombre): # La tarea estará expresada con el índice +1
        tarea.nombre = nuevo_nombre

    def modificarDescripcionTarea(self, tarea, nueva_descripcion):
        tarea.descripcion = nueva_descripcion

    def agregarFechaVencimientoATarea(self, tarea, nueva_fecha_vencimiento):
        tarea.fecha_vencimiento = nueva_fecha_vencimiento

    def quitarFechaVencimientoDeTarea(self, tarea):
        del tarea.fecha_vencimiento

        if not self.tareas:
            return "No hay tareas en esta lista."
        else:
            return print(self.tareas)
    
    def __str__(self):
        if not self.tareas:
            print("No hay tareas en esta lista.")
        else:
            print("Tareas:")
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea}")