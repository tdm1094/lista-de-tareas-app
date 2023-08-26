class Tarea:

# Constructor

    def __init__(self, nombre, descripcion, fechaVencimiento):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fechaVencimiento = fechaVencimiento

# Getters
 
    def get_nombre(self):
        return self.__nombre
    
    def get_descripcion(self):
        return self.__descripcion
        
    def get_echaVencimiento(self):
        return self.__fechaVencimiento
        
# Setters

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
        
    def set_descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion
        
    def fechaVencimiento(self, nueva_fecha):
        self._fechaVencimiento = nueva_fecha