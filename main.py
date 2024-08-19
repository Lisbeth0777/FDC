from services.estudiante_service import create_estudiante, read_estudiante, update_estudiante, delete_estudiante
from services.ejercicio_service import create_ejercicio, read_ejercicio, update_ejercicio, delete_ejercicio
from services.ejecucion_service import create_ejecucion, read_ejecucion, update_ejecucion, delete_ejecucion

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Gestionar Estudiantes")
    print("2. Gestionar Ejercicios")
    print("3. Gestionar Ejecuciones")
    print("4. Salir")

def gestionar_estudiantes():
    while True:
        print("\n--- Gestión de Estudiantes ---")
        print("1. Crear Estudiante")
        print("2. Leer Estudiante")
        print("3. Actualizar Estudiante")
        print("4. Eliminar Estudiante")
        print("5. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            email = input("Email del estudiante: ")
            estudiante = create_estudiante(nombre=nombre, email=email)
            print(f"Estudiante creado: {estudiante.__dict__}")

        elif opcion == "2":
            estudiante_id = int(input("ID del estudiante a leer: "))
            estudiante = read_estudiante(estudiante_id)
            print(estudiante.__dict__ if estudiante else "Estudiante no encontrado")

        elif opcion == "3":
            estudiante_id = int(input("ID del estudiante a actualizar: "))
            nombre = input("Nuevo nombre del estudiante: ")
            email = input("Nuevo email del estudiante: ")
            estudiante = update_estudiante(estudiante_id, nombre_completo=nombre, email=email)
            print(estudiante.__dict__ if estudiante else "Estudiante no encontrado")

        elif opcion == "4":
            estudiante_id = int(input("ID del estudiante a eliminar: "))
            delete_estudiante(estudiante_id)
            print("Estudiante eliminado.")

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

def gestionar_ejercicios():
    while True:
        print("\n--- Gestión de Ejercicios ---")
        print("1. Crear Ejercicio")
        print("2. Leer Ejercicio")
        print("3. Actualizar Ejercicio")
        print("4. Eliminar Ejercicio")
        print("5. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del ejercicio: ")
            descripcion = input("Descripción del ejercicio: ")
            ejercicio = create_ejercicio(nombre=nombre, descripcion=descripcion)
            print(f"Ejercicio creado: {ejercicio.__dict__}")

        elif opcion == "2":
            ejercicio_id = int(input("ID del ejercicio a leer: "))
            ejercicio = read_ejercicio(ejercicio_id)
            print(ejercicio.__dict__ if ejercicio else "Ejercicio no encontrado")

        elif opcion == "3":
            ejercicio_id = int(input("ID del ejercicio a actualizar: "))
            nombre = input("Nuevo nombre del ejercicio: ")
            descripcion = input("Nueva descripción del ejercicio: ")
            ejercicio = update_ejercicio(ejercicio_id, nombre=nombre, descripcion=descripcion)
            print(ejercicio.__dict__ if ejercicio else "Ejercicio no encontrado")

        elif opcion == "4":
            ejercicio_id = int(input("ID del ejercicio a eliminar: "))
            delete_ejercicio(ejercicio_id)
            print("Ejercicio eliminado.")

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

def gestionar_ejecuciones():
    while True:
        print("\n--- Gestión de Ejecuciones ---")
        print("1. Crear Ejecución")
        print("2. Leer Ejecución")
        print("3. Actualizar Ejecución")
        print("4. Eliminar Ejecución")
        print("5. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            estudiante_id = int(input("ID del estudiante: "))
            ejercicio_id = int(input("ID del ejercicio: "))
            numero_series = int(input("Número de series: "))
            numero_repeticiones = int(input("Número de repeticiones: "))
            peso_barra = float(input("Peso de la barra: "))
            peso_discos = float(input("Peso de los discos: "))
            porcentaje = float(input("Porcentaje (opcional, dejar en blanco si no aplica): ") or 0)
            ejecucion = create_ejecucion(estudiante_id, ejercicio_id, numero_series, numero_repeticiones,
                                         peso_barra, peso_discos, porcentaje)
            print(f"Ejecución creada: {ejecucion.__dict__}")

        elif opcion == "2":
            ejecucion_id = int(input("ID de la ejecución a leer: "))
            ejecucion = read_ejecucion(ejecucion_id)
            print(ejecucion.__dict__ if ejecucion else "Ejecución no encontrada")

        elif opcion == "3":
            ejecucion_id = int(input("ID de la ejecución a actualizar: "))
            numero_series = input("Nuevo número de series (dejar en blanco si no aplica): ")
            numero_repeticiones = input("Nuevo número de repeticiones (dejar en blanco si no aplica): ")
            peso_barra = input("Nuevo peso de la barra (dejar en blanco si no aplica): ")
            peso_discos = input("Nuevo peso de los discos (dejar en blanco si no aplica): ")
            porcentaje = input("Nuevo porcentaje (dejar en blanco si no aplica): ")

            update_data = {}
            if numero_series:
                update_data['numero_series'] = int(numero_series)
            if numero_repeticiones:
                update_data['numero_repeticiones'] = int(numero_repeticiones)
            if peso_barra:
                update_data['peso_barra'] = float(peso_barra)
            if peso_discos:
                update_data['peso_discos'] = float(peso_discos)
            if porcentaje:
                update_data['porcentaje'] = float(porcentaje)

            ejecucion = update_ejecucion(ejecucion_id, **update_data)
            print(ejecucion.__dict__ if ejecucion else "Ejecución no encontrada")

        elif opcion == "4":
            ejecucion_id = int(input("ID de la ejecución a eliminar: "))
            delete_ejecucion(ejecucion_id)
            print("Ejecución eliminada.")

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            gestionar_estudiantes()
        elif opcion == "2":
            gestionar_ejercicios()
        elif opcion == "3":
            gestionar_ejecuciones()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
