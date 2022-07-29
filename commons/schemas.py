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
