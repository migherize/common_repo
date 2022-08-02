class Persona:
    """Clase que representa una Persona"""
    
    def __init__(self, cedula, nombre, apellido, sexo):
        """Constructor de clase Persona"""
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def hablar(self, mensaje):
        """Mostrar mensaje de saludo de Persona"""
        return mensaje

class Animal:
    """Clase que representa una Animal"""
    
    def __init__(self, dueño, nombre, tipo, sexo):
        """Constructor de clase Persona"""
        self.dueño = dueño
        self.nombre = nombre
        self.tipo = tipo
        self.sexo = sexo

    def Come(self, mensaje):
        """Mostrar mensaje de saludo de Persona"""
        return mensaje