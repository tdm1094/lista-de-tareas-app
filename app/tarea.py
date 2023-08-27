import datetime


class Tarea:
    def __init__(self, nombre, descripcion=None, fecha_vencimiento=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = False

    def __str__(self):
        return f"Nombre: {self.nombre}\n" \
               f"Descripción: {self.descripcion}\n" \
               f"Fecha de vencimiento: {self.fecha_vencimiento}\n" \
               f"Estado: {self.estado}"

    def cambiar_estado(self):
        self.estado = not self.estado

    def esta_vencida(self):
        return self.fecha_vencimiento < datetime.datetime.now()
