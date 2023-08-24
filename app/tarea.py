class Tarea:
# Constructor
    def __init__(self, nombre, descripcion, fechaVencimiento):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaVencimiento = fechaVencimiento

# Getters
    @property
    def nombre(self):
        return self.nombre
    
    @property
    def descripcion(self):
        return self.descripcion
    
    @property
    def fechaVencimiento(self):
        return self.fechaVencimiento
    
# Setters
    @nombre.setter
    def nombre(self):
        return self.nombre
    
    @descripcion.setter
    def descripcion(self):
        return self.descripcion
    
    @fechaVencimiento.setter
    def fechaVencimiento(self):
        return self.fechaVencimiento