from data.repositorio import RepositorioTurnos
from models.profesional import Profesional
from models.cliente import Cliente
from models.cita import Cita


class ServicioTurnos:
    """
    Contiene la lógica de negocio del sistema de turnos.
    """

    def __init__(self, repositorio=None):
        self.repositorio = repositorio or RepositorioTurnos()

    # -----------------------------
    # PROFESIONALES
    # -----------------------------

    def crear_profesional(self, nombre, especialidad, horario):
        """
        Crea un profesional válido y lo guarda en el repositorio.
        """
        profesional = Profesional(
            nombre=nombre,
            especialidad=especialidad,
            horario=horario
        )

        profesional_dict = {
            "nombre": profesional.nombre,
            "especialidad": profesional.especialidad,
            "horario": profesional.horario
        }

        self.repositorio.guardar_profesional(profesional_dict)
        return profesional

    def obtener_profesional_por_nombre(self, nombre):
        """
        Devuelve un profesional existente a partir de su nombre.
        """
        profesionales = self.repositorio.obtener_profesionales()

        for profesional_dict in profesionales:
            if profesional_dict["nombre"].lower() == nombre.lower():
                return Profesional(
                    nombre=profesional_dict["nombre"],
                    especialidad=profesional_dict["especialidad"],
                    horario=profesional_dict["horario"]
                )

        raise ValueError("No existe ningún profesional con ese nombre")

    # -----------------------------
    # CLIENTES
    # -----------------------------

    def crear_cliente(self, nombre, edad):
        """
        Crea un cliente válido y lo guarda en el repositorio.
        """
        cliente = Cliente(
            nombre=nombre,
            edad=edad
        )

        cliente_dict = {
            "nombre": cliente.nombre,
            "edad": cliente.edad
        }

        self.repositorio.guardar_cliente(cliente_dict)
        return cliente

    def obtener_cliente_por_nombre(self, nombre):
        """
        Devuelve un cliente existente a partir de su nombre.
        """
        clientes = self.repositorio.obtener_clientes()

        for cliente_dict in clientes:
            if cliente_dict["nombre"].lower() == nombre.lower():
                return Cliente(
                    nombre=cliente_dict["nombre"],
                    edad=cliente_dict["edad"]
                )

        raise ValueError("No existe ningún cliente con ese nombre")

    # -----------------------------
    # CITAS
    # -----------------------------

    def crear_cita(self, profesional, cliente, fecha, hora_inicio):
        """
        Crea una cita válida, comprueba solapamientos y la guarda.
        """
        # 1. Crear la cita (validación de modelo)
        cita = Cita(
            profesional=profesional,
            cliente=cliente,
            fecha=fecha,
            hora_inicio=hora_inicio
        )

        # 2. Obtener citas existentes
        citas_existentes = self.repositorio.obtener_citas()

        # 3. Comprobar solapamientos
        for cita_existente in citas_existentes:
            if cita_existente["profesional"] != cita.profesional.nombre:
                continue

            if cita_existente["fecha"] != cita.fecha.isoformat():
                continue

            if cita_existente["hora_inicio"] == cita.hora_inicio.strftime("%H:%M"):
                raise ValueError(
                    "El profesional ya tiene una cita en esa fecha y hora"
                )

        # 4. Guardar la cita
        cita_dict = {
            "profesional": cita.profesional.nombre,
            "cliente": cita.cliente.nombre,
            "fecha": cita.fecha.isoformat(),
            "hora_inicio": cita.hora_inicio.strftime("%H:%M"),
            "duracion": cita.duracion
        }

        self.repositorio.guardar_cita(cita_dict)
        return cita

    def cancelar_cita(self, profesional, fecha, hora_inicio):
        """
        Cancela (elimina) una cita existente.
        """
        citas_existentes = self.repositorio.obtener_citas()
        cita_encontrada = False

        # 1. Comprobar que la cita existe
        for cita_existente in citas_existentes:
            if (
                cita_existente["profesional"] == profesional.nombre
                and cita_existente["fecha"] == fecha.isoformat()
                and cita_existente["hora_inicio"] == hora_inicio.strftime("%H:%M")
            ):
                cita_encontrada = True
                break

        if not cita_encontrada:
            raise ValueError("No existe ninguna cita con esos datos")

        # 2. Eliminar la cita
        nuevas_citas = []

        for cita_existente in citas_existentes:
            if (
                cita_existente["profesional"] == profesional.nombre
                and cita_existente["fecha"] == fecha.isoformat()
                and cita_existente["hora_inicio"] == hora_inicio.strftime("%H:%M")
            ):
                continue

            nuevas_citas.append(cita_existente)

        # 3. Guardar cambios
        datos = self.repositorio._leer_datos()
        datos["citas"] = nuevas_citas
        self.repositorio._escribir_datos(datos)

    # -----------------------------
    # CONSULTAS
    # -----------------------------

    def ver_agenda_profesional(self, profesional):
        """
        Devuelve la agenda del profesional ordenada por fecha y hora.
        """
        citas_existentes = self.repositorio.obtener_citas()

        agenda = []
        for cita_existente in citas_existentes:
            if cita_existente["profesional"] == profesional.nombre:
                agenda.append(cita_existente)

        agenda_ordenada = sorted(
            agenda,
            key=lambda cita: (cita["fecha"], cita["hora_inicio"])
        )

        return agenda_ordenada
