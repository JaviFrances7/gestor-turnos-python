from services.turnos import ServicioTurnos
from datetime import datetime


def ejecutar():
    """
    Función principal de la interfaz de línea de comandos.
    """
    servicio = ServicioTurnos()

    while True:
        print("\n--- SISTEMA DE TURNOS ---")
        print("1. Crear profesional")
        print("2. Crear cliente")
        print("3. Crear cita")
        print("4. Ver agenda de un profesional")
        print("5. Cancelar cita")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_profesional(servicio)

        elif opcion == "2":
            crear_cliente(servicio)

        elif opcion == "3":
            crear_cita(servicio)

        elif opcion == "4":
            ver_agenda_profesional(servicio)

        elif opcion == "5":
            cancelar_cita(servicio)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


# ----------------------------------
# OPCIONES DEL MENÚ
# ----------------------------------

def crear_profesional(servicio):
    """
    Crea un profesional pidiendo datos al usuario.
    """
    try:
        nombre = input("Nombre del profesional: ")
        especialidad = input("Especialidad: ")
        horario = input("Horario (ej: 09:00-14:00): ")

        profesional = servicio.crear_profesional(
            nombre=nombre,
            especialidad=especialidad,
            horario=horario
        )

        print("\nProfesional creado correctamente:")
        print(f"- Nombre: {profesional.nombre}")
        print(f"- Especialidad: {profesional.especialidad}")

    except Exception as error:
        print(f"\nError al crear profesional: {error}")


def crear_cliente(servicio):
    """
    Crea un cliente pidiendo datos al usuario.
    """
    try:
        nombre = input("Nombre del cliente: ")
        edad = int(input("Edad: "))

        cliente = servicio.crear_cliente(
            nombre=nombre,
            edad=edad
        )

        print("\nCliente creado correctamente:")
        print(f"- Nombre: {cliente.nombre}")
        print(f"- Edad: {cliente.edad}")

    except Exception as error:
        print(f"\nError al crear cliente: {error}")


def crear_cita(servicio):
    """
    Crea una cita pidiendo datos al usuario.
    """
    try:
        nombre_profesional = input("Nombre del profesional: ")
        nombre_cliente = input("Nombre del cliente: ")
        fecha_texto = input("Fecha (DD-MM-YYYY): ")
        hora_texto = input("Hora inicio (HH:MM): ")

        # Obtener profesional y cliente reales
        profesional = servicio.obtener_profesional_por_nombre(nombre_profesional)
        cliente = servicio.obtener_cliente_por_nombre(nombre_cliente)

        cita = servicio.crear_cita(
            profesional=profesional,
            cliente=cliente,
            fecha=fecha_texto,
            hora_inicio=hora_texto
        )

        print("\nCita creada correctamente:")
        print(
            f"{cita.fecha} | {cita.hora_inicio.strftime('%H:%M')} | "
            f"{cita.profesional.nombre} - {cita.cliente.nombre}"
        )

    except Exception as error:
        print(f"\nError al crear cita: {error}")


def ver_agenda_profesional(servicio):
    """
    Muestra la agenda de un profesional.
    """
    try:
        nombre_profesional = input("Nombre del profesional: ")

        profesional = servicio.obtener_profesional_por_nombre(nombre_profesional)
        agenda = servicio.ver_agenda_profesional(profesional)

        if not agenda:
            print("\nNo hay citas para este profesional.")
            return

        print("\n--- AGENDA DEL PROFESIONAL ---")
        for cita in agenda:
            print(
                f"{cita['fecha']} | {cita['hora_inicio']} | "
                f"Cliente: {cita['cliente']}"
            )

    except Exception as error:
        print(f"\nError al mostrar agenda: {error}")


def cancelar_cita(servicio):
    """
    Cancela una cita existente.
    """
    try:
        nombre_profesional = input("Nombre del profesional: ")
        fecha_texto = input("Fecha (DD-MM-YYYY): ")
        hora_texto = input("Hora inicio (HH:MM): ")

        profesional = servicio.obtener_profesional_por_nombre(nombre_profesional)

        fecha = datetime.strptime(fecha_texto, "%d-%m-%Y").date()
        hora = datetime.strptime(hora_texto, "%H:%M").time()

        servicio.cancelar_cita(
            profesional=profesional,
            fecha=fecha,
            hora_inicio=hora
        )

        print("\nCita cancelada correctamente.")

    except Exception as error:
        print(f"\nError al cancelar cita: {error}")
