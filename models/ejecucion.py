from typing import Optional
from datetime import datetime

class Ejecucion:
    def __init__(self, id: int, estudiante_id: int, ejercicio_id: int, fecha: datetime = datetime.now(),
                 numero_series: int = 0, numero_repeticiones: int = 0, peso_barra: float = 0.0,
                 peso_discos: float = 0.0, porcentaje: Optional[float] = None):
        self.id = id
        self.estudiante_id = estudiante_id
        self.ejercicio_id = ejercicio_id
        self.fecha = fecha
        self.numero_series = numero_series
        self.numero_repeticiones = numero_repeticiones
        self.peso_barra = peso_barra
        self.peso_discos = peso_discos
        self.porcentaje = porcentaje
