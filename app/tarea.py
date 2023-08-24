class Tarea:
# Constructor
    def __init__(self, nombre, descripcion, fechaVencimiento):
        self._nombre = nombre
        self._descripcion = descripcion
        self._fechaVencimiento = fechaVencimiento

# Getters
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def descripcion(self):
        return self._descripcion
    
    @property
    def fechaVencimiento(self):
        return self._fechaVencimiento
    
# Setters
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion
    
    @fechaVencimiento.setter
    def fechaVencimiento(self, nueva_fecha):
        self._fechaVencimiento = nueva_fecha