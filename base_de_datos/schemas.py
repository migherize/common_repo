class Contratista:
    """Clase que representa una Contratista"""
    
    def __init__(self, licencia, nombre, apellido, ciudad):
        """Constructor de clase Contratista"""
        self.licencia = licencia
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad

    def hablar(self, mensaje):
        """Mostrar mensaje de saludo de Contratista"""
        return mensaje