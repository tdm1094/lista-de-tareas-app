from app.Menues.menu_principal import MenuPrincipal
from app.lista_de_tareas import ListaDeTareas


def main():
    lista = ListaDeTareas("lista_inicial")

    MenuPrincipal.mostrar_logo()
    MenuPrincipal.run(lista)


if __name__ == "__main__":
    main()
