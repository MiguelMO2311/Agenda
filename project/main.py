
import interface
from logic import command_interface, Agenda
from utils import crear_interfaz

def main():
    agenda = Agenda()  # Crear una instancia de Agenda
    while True:
        print(interface.INTERFAZ_BASE)
        eleccion = crear_interfaz()
        while not 1 <= eleccion <= 5:
            print(interface.INTERFAZ_ELECCION_ERRONEA)
            eleccion = crear_interfaz()
        comando = command_interface[eleccion]
        if eleccion == 5:
            comando()  # Llamar a la función about sin argumentos
        else:
            comando(agenda)  # Pasar la instancia de Agenda a las otras funciones
        eleccion_salir = input(interface.INTERFAZ_SALIDA)
        if eleccion_salir.lower() not in ("si", "s", "yes", "y"):
            break

if __name__ == "__main__":
    main()