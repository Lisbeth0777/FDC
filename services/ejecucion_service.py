from models.ejecucion import Ejecucion
from typing import List, Optional
from datetime import datetime

# Almacenamiento en memoria
ejecuciones: List[Ejecucion] = []

# Ejecuciones CRUD

def create_ejecucion(estudiante_id: int, ejercicio_id: int, numero_series: int, numero_repeticiones: int,
                     peso_barra: float, peso_discos: float, porcentaje: Optional[float] = None):
    id = len(ejecuciones) + 1
    ejecucion = Ejecucion(id, estudiante_id, ejercicio_id, numero_series=numero_series,
                          numero_repeticiones=numero_repeticiones, peso_barra=peso_barra,
                          peso_discos=peso_discos, porcentaje=porcentaje)
    ejecuciones.append(ejecucion)
    return ejecucion

def read_ejecucion(ejecucion_id: int):
    return next((ej for ej in ejecuciones if ej.id == ejecucion_id), None)

def update_ejecucion(ejecucion_id: int, **kwargs):
    ejecucion = read_ejecucion(ejecucion_id)
    if ejecucion:
        for key, value in kwargs.items():
            setattr(ejecucion, key, value)
        return ejecucion
    return None

def delete_ejecucion(ejecucion_id: int):
    global ejecuciones
    ejecuciones = [ej for ej in ejecuciones if ej.id != ejecucion_id]
