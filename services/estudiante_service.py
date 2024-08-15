from models.estudiante import Estudiante
from typing import List, Optional

# Almacenamiento en memoria
estudiantes: List[Estudiante] = []

# Estudiantes CRUD

def create_estudiante(nombre: str, email: str, **kwargs):
    id = len(estudiantes) + 1
    estudiante = Estudiante(id, nombre, email, **kwargs)
    estudiantes.append(estudiante)
    return estudiante

def read_estudiante(estudiante_id: int):
    return next((est for est in estudiantes if est.id == estudiante_id), None)

def update_estudiante(estudiante_id: int, **kwargs):
    estudiante = read_estudiante(estudiante_id)
    if estudiante:
        for key, value in kwargs.items():
            setattr(estudiante, key, value)
        return estudiante
    return None

def delete_estudiante(estudiante_id: int):
    global estudiantes
    estudiantes = [est for est in estudiantes if est.id != estudiante_id]
