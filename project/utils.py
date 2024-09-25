import interface

def crear_interfaz():
    try:
        return int(input(interface.INTERFAZ_ELECCION))
    except ValueError:
        return 10000  # Valor incorrecto para que falle
