class ListaDeTareas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def __str__(self):
        if not self.tareas:
            print("No hay tareas en esta lista.")
        else:
            print("Tareas:")
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea}")

    def agregar_tarea_nueva(self, nueva_tarea):
        self.tareas.append(nueva_tarea)

    def eliminar_tarea(self, indice_tarea):
        del self.tareas[indice_tarea]

    def modificar_tarea_nombre(self, indice_tarea, nuevo_nombre):
        self.tareas[indice_tarea].nombre = nuevo_nombre

    def modificar_tarea_descripcion(self, indice_tarea, nueva_descripcion):
        self.tareas[indice_tarea].descripcion = nueva_descripcion

    def agregar_o_modificar_tarea_fecha_vencimiento(self, indice_tarea, nueva_fecha_vencimiento):
        self.tareas[indice_tarea].fecha_vencimiento = nueva_fecha_vencimiento

    def eliminar_tarea_fecha_vencimiento(self, indice_tarea):
        self.tareas[indice_tarea].fecha_vencimiento = None

    def cambiar_estado_tarea(self, indice_tarea):
        self.tareas[indice_tarea].cambiar_estado()

    def __str__(self):
        if not self.tareas:
            print("No hay tareas en esta lista.")
        else:
            print("Tareas:")
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea}")
