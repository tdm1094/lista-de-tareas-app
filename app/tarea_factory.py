from app.tarea import Tarea


class TareaFactory:
    @staticmethod
    def construir_tarea(nombre, descripcion=None, fecha_vencimiento=None):
        return Tarea(nombre, descripcion, fecha_vencimiento)
