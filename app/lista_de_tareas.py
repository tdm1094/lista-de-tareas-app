from tarea import Tarea


class ListaDeTareas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea_nueva(self, nombre, descripcion, fecha_vencimiento):
        tarea = Tarea(nombre, descripcion, fecha_vencimiento)
        self.tareas.append(tarea)

    def eliminar_tarea(self, tarea):
        self.tareas.remove(tarea)

    def modificar_tarea_nombre(self, tarea, nuevo_nombre):  # La tarea estará expresada con el índice +1
        tarea.nombre = nuevo_nombre

    def modificar_tarea_descripcion(self, tarea, nueva_descripcion):
        tarea.descripcion = nueva_descripcion

    def agregar_tarea_nueva_fecha_vencimiento(self, tarea, nueva_fecha_vencimiento):
        tarea.fecha_vencimiento = nueva_fecha_vencimiento

    def eliminar_tarea_fecha_vencimiento(self, tarea):
        del tarea.fecha_vencimiento

    def __str__(self):
        if not self.tareas:
            print("No hay tareas en esta lista.")
        else:
            print("Tareas:")
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea}")
