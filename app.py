from services.estudiante_service import create_estudiante, read_estudiante, update_estudiante, delete_estudiante
from services.ejercicio_service import create_ejercicio, read_ejercicio, update_ejercicio, delete_ejercicio
from services.ejecucion_service import create_ejecucion, read_ejecucion, update_ejecucion, delete_ejecucion

# Ejemplo de uso del CRUD

# Crear un estudiante
nuevo_estudiante = create_estudiante(nombre="Juan Pérez", email="juan@example.com")
print(nuevo_estudiante.__dict__)

# Leer un estudiante
estudiante = read_estudiante(1)
print(estudiante.__dict__ if estudiante else "Estudiante no encontrado")

# Actualizar un estudiante
estudiante_actualizado = update_estudiante(1, nombre_completo="Juan Carlos Pérez")
print(estudiante_actualizado.__dict__ if estudiante_actualizado else "Estudiante no encontrado")

# Eliminar un estudiante
delete_estudiante(1)
estudiante = read_estudiante(1)
print(estudiante.__dict__ if estudiante else "Estudiante no encontrado")
