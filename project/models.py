import json

class Contacto:
    def __init__(self, nombre: str, telefono: str, email: str):
        if not self.validar_telefono(telefono):
            raise ValueError(f"Teléfono inválido: {telefono}")
        if not self.validar_email(email):
            raise ValueError(f"Email inválido: {email}")
        
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def mostrar_info(self) -> str:
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

    def a_json(self) -> str:
        return json.dumps(self.__dict__)

    @staticmethod
    def validar_telefono(telefono: str) -> bool:
        # Validar que el teléfono tenga exactamente 11 caracteres (incluyendo espacios)
        if len(telefono) != 11:
            return False
        # Validar que los caracteres en las posiciones correctas sean espacios
        if telefono[3] != ' ' or telefono[7] != ' ':
            return False
        # Validar que los otros caracteres sean dígitos
        for i in range(11):
            if i != 3 and i != 7 and not telefono[i].isdigit():
                return False
        return True

    @staticmethod
    def validar_email(email: str) -> bool:
        # Validar que el email contenga exactamente un '@' y al menos un '.'
        if email.count('@') != 1 or '.' not in email.split('@')[1]:
            return False
        # Validar que el email no comience ni termine con un punto
        if email.startswith('.') or email.endswith('.'):
            return False
        # Validar que el email no tenga espacios
        if ' ' in email:
            return False
        return True
