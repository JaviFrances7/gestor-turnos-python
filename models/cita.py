from datetime import datetime, time
from models.profesional import Profesional
from models.cliente import Cliente


class Cita:
    """
    Representa una cita entre un cliente y un profesional.
    """

    def __init__(self, profesional, cliente, fecha, hora_inicio, duracion=1):
        self.profesional = self.validar_profesional(profesional)
        self.cliente = self.validar_cliente(cliente)
        self.fecha = self.validar_fecha(fecha)
        self.hora_inicio = self.validar_hora(hora_inicio)
        self.duracion = duracion

    def validar_profesional(self, profesional):
        if not isinstance(profesional, Profesional):
            raise TypeError("El profesional debe ser un objeto Profesional")
        return profesional

    def validar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("El cliente debe ser un objeto Cliente")
        return cliente

    def validar_fecha(self, fecha):
        if isinstance(fecha, datetime):
            return fecha.date()

        if isinstance(fecha, str):
            try:
                return datetime.strptime(fecha, "%d-%m-%Y").date()
            except ValueError:
                raise ValueError("La fecha debe tener el formato DD-MM-YYYY")

        raise TypeError("La fecha debe ser un texto o datetime")

    def validar_hora(self, hora):
        if isinstance(hora, time):
            return hora

        if isinstance(hora, str):
            try:
                return datetime.strptime(hora, "%H:%M").time()
            except ValueError:
                raise ValueError("La hora debe tener el formato HH:MM")

        raise TypeError("La hora debe ser un texto o time")
