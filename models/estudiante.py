from typing import Optional
class Estudiante:
    def __init__(self, id: int, nombre: str, email: str, nombre_completo: Optional[str] = None,
                 cedula: Optional[str] = None, telefono_emergencia: Optional[str] = None,
                 tipo_sangre: Optional[str] = None, disciplina: str = 'halterofilia',
                 foto: Optional[bytes] = None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.nombre_completo = nombre_completo
        self.cedula = cedula
        self.telefono_emergencia = telefono_emergencia
        self.tipo_sangre = tipo_sangre
        self.disciplina = disciplina
        self.foto = foto
