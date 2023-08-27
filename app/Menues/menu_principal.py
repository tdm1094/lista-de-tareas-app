import datetime

from app.Menues.menu_tareas import MenuTareas
from app.tarea_factory import TareaFactory


class MenuPrincipal:
    def __init__(self):
        self.opciones = {}
        self.agregar_opcion("Listar tareas", self.opcion_listar_tareas)
        self.agregar_opcion("Agregar tarea", self.opcion_agregar_tarea)
        self.agregar_opcion("Modificar tarea", self.opcion_modificar_tarea)
        self.agregar_opcion("Eliminar tarea", self.opcion_eliminar_tarea)
        self.agregar_opcion("Salir de la aplicación", self.opcion_salir_aplicacion)

    @staticmethod
    def mostrar_logo():
        print("""
            ████████ ██    ██ ██████  ██    ██ 
               ██    ██    ██ ██   ██ ██    ██ 
               ██    ██    ██ ██   ██ ██    ██ 
               ██    ██    ██ ██   ██ ██    ██ 
               ██     ██████  ██████   ██████  
                   
                      by ToManu Corp.                                   
            """)

    def agregar_opcion(self, texto_opcion, metodo_a_ejecutar):
        self.opciones[len(self.opciones) + 1] = (texto_opcion, metodo_a_ejecutar)

    def mostrar(self):
        print("Menu Principal:")
        for numero_opcion, (texto_opcion, _) in self.opciones.items():
            print(f"{numero_opcion}. {texto_opcion}")

    def opcion_listar_tareas(self):
        MenuTareas.run()

    def opcion_agregar_tarea(self):
        print("Creación de tarea: ")

        tarea_nueva_nombre = input("Nombre de tarea: ")
        tarea_nueva_descripcion = input("Descripcion de tarea: ")
        tarea_nueva_tiene_vencimiento = input("¿Tiene vencimiento? [s/n]")

        tarea_nueva_fecha_vencimiento = self.opcion_agregar_vencimiento() if tarea_nueva_tiene_vencimiento == "s" else None

        TareaFactory.construir_tarea(tarea_nueva_nombre, tarea_nueva_descripcion, tarea_nueva_fecha_vencimiento)

    def opcion_agregar_vencimiento(self):
        print("Introducir fechas usando el formato '1999/12/31'")
        dia_vencimiento = input("Día del vencimiento: ")
        mes_vencimiento = input("Mes del vencimiento: ")
        anio_vencimiento = input("Año del vencimiento: ")
        fecha_vencimiento_str = f"{anio_vencimiento}/{mes_vencimiento}/{dia_vencimiento}"

        return datetime.datetime.strptime(fecha_vencimiento_str, '%y/%m/%d')

    def opcion_modificar_tarea(self):
        print("You selected Option 3")

    def run(self, lista_tareas):
        self.mostrar()
        choice = input("Seleccionar opción: ")

        try:
            choice = int(choice)
            if choice in self.opciones:
                _, method = self.opciones[choice]
                method()
            else:
                print("Número de opción inválido.")
        except ValueError:
            print("Entrada errónea. Por favor, introducir un número de opción.")
