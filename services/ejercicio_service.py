from models.ejercicio import Ejercicio
from typing import List, Optional

# Almacenamiento en memoria
ejercicios: List[Ejercicio] = []

# Ejercicios CRUD

def create_ejercicio(nombre: str, **kwargs):
    id = len(ejercicios) + 1
    ejercicio = Ejercicio(id, nombre, **kwargs)
    ejercicios.append(ejercicio)
    return ejercicio

def read_ejercicio(ejercicio_id: int):
    return next((ej for ej in ejercicios if ej.id == ejercicio_id), None)

def update_ejercicio(ejercicio_id: int, **kwargs):
    ejercicio = read_ejercicio(ejercicio_id)
    if ejercicio:
        for key, value in kwargs.items():
            setattr(ejercicio, key, value)
        return ejercicio
    return None

def delete_ejercicio(ejercicio_id: int):
    global ejercicios
    ejercicios = [ej for ej in ejercicios if ej.id != ejercicio_id]
