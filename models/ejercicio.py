from typing import Optional
class Ejercicio:
    def __init__(self, id: int, nombre: str, descripcion: Optional[str] = None, tipo: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
