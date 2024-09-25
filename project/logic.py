import os
import json
from database.contactos import contactos  # Importar los contactos cargados
import interface
from settings import VERSION
from models import Contacto

class Agenda:
    def __init__(self):
        self.contactos = [Contacto(**contacto) for contacto in contactos]  # Inicializar con los contactos cargados

    def agregar_contacto(self, contacto: Contacto):
        self.contactos.append(contacto)
        self.guardar_contacto_json(contacto)
        self.actualizar_contactos_py()

    def mostrar_contactos(self):
        for contacto in self.contactos:
            print(contacto.mostrar_info())

    def actualizar_contacto(self, nombre: str, nuevo_nombre: str = None, nuevo_telefono: str = None, nuevo_email: str = None) -> bool:
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                if nuevo_nombre:
                    contacto.nombre = nuevo_nombre
                if nuevo_telefono:
                    if not Contacto.validar_telefono(nuevo_telefono):
                        raise ValueError(f"Teléfono inválido: {nuevo_telefono}")
                    contacto.telefono = nuevo_telefono
                if nuevo_email:
                    if not Contacto.validar_email(nuevo_email):
                        raise ValueError(f"Email inválido: {nuevo_email}")
                    contacto.email = nuevo_email
                self.guardar_contacto_json(contacto)
                self.actualizar_contactos_py()
                return True
        return False

    def guardar_contacto_json(self, contacto: Contacto):
        # Definir la ruta del archivo
        archivo_path = f'contacto_{contacto.nombre}.json'
        # Guardar el contacto en un archivo JSON
        with open(archivo_path, 'w') as archivo:
            json.dump(contacto.__dict__, archivo, ensure_ascii=False, indent=4)

    def eliminar_contacto(self, nombre: str) -> bool:
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                # Eliminar el archivo JSON si existe
                archivo_path = f'contacto_{contacto.nombre}.json'
                if os.path.exists(archivo_path):
                    os.remove(archivo_path)
                self.actualizar_contactos_py()
                return True
        return False

    def actualizar_contactos_py(self):
        contactos_dict = [contacto.__dict__ for contacto in self.contactos]
        # Crear la carpeta si no existe
        os.makedirs('database', exist_ok=True)
        # Guardar los contactos en el archivo contactos.py
        with open('./contactos.py', 'w') as archivo:
            archivo.write(f"contactos = {json.dumps(contactos_dict, ensure_ascii=False, indent=4)}")

def read(agenda: Agenda):
    print(interface.LEER_CONTACTO)
    agenda.mostrar_contactos()

def create(agenda: Agenda):
    print(interface.CREAR_CONTACTO)
    nombre_contacto = input(interface.CREAR_CONTACTO_NOMBRE)
    telefono_contacto = input(interface.CREAR_CONTACTO_TELEFONO)
    email_contacto = input(interface.CREAR_CONTACTO_EMAIL)
    contacto = Contacto(nombre_contacto, telefono_contacto, email_contacto)
    agenda.agregar_contacto(contacto)
    print("Contacto creado exitosamente.")
    print(contacto.a_json())  # Convertir a JSON y mostrar

def update(agenda: Agenda):
    print(interface.ACTUALIZAR_CONTACTO)
    nombre_contacto = input(interface.ACTUALIZAR_CONTACTO_NOMBRE)
    nuevo_nombre = input(interface.ACTUALIZAR_CONTACTO_NUEVO_NOMBRE)
    nuevo_telefono = input(interface.ACTUALIZAR_CONTACTO_NUEVO_TELEFONO)
    nuevo_email = input(interface.ACTUALIZAR_CONTACTO_NUEVO_EMAIL)
    if agenda.actualizar_contacto(nombre_contacto, nuevo_nombre, nuevo_telefono, nuevo_email):
        print("Contacto actualizado exitosamente.")
    else:
        print("Contacto no encontrado.")

def delete(agenda: Agenda):
    print(interface.ELIMINAR_CONTACTO)
    nombre_contacto = input(interface.ELIMINAR_CONTACTO_NOMBRE)
    if agenda.eliminar_contacto(nombre_contacto):
        print("Contacto eliminado exitosamente.")
    else:
        print("Contacto no encontrado.")

def about():
    print(f"La version actual es {VERSION}")

# Ejemplo de uso
agenda = Agenda()

command_interface = {
    1: read,
    2: create,
    3: update,
    4: delete,
    5: about
}
