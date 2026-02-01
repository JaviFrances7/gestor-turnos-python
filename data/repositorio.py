import json
from pathlib import Path


class RepositorioTurnos:
    """
    Gestiona los turnos.
    Se encarga de guardar y recuperar turnos desde un archivo JSON.
    """

    def __init__(self, ruta_archivo="data/turnos.json"):
        self.ruta_archivo = Path(ruta_archivo)
        self._asegurar_archivo()

    def _asegurar_archivo(self):
        """
        Asegura que el archivo de datos existe.
        Si no existe, lo crea con la estructura inicial.
        """
        if not self.ruta_archivo.exists():
            self.ruta_archivo.parent.mkdir(parents=True, exist_ok=True)

            datos_iniciales = {
                "profesionales": [],
                "clientes": [],
                "citas": []
            }

            with self.ruta_archivo.open("w", encoding="utf-8") as archivo:
                json.dump(datos_iniciales, archivo, ensure_ascii=False, indent=4)

    def _leer_datos(self):
        """
        Lee y devuelve todo el contenido del archivo JSON.
        """
        with self.ruta_archivo.open("r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def obtener_profesionales(self):
        """
        Devuelve la lista de profesionales almacenados.
        """
        datos = self._leer_datos()
        return datos["profesionales"]

    def obtener_clientes(self):
        """
        Devuelve la lista de clientes almacenados.
        """
        datos = self._leer_datos()
        return datos["clientes"]

    def obtener_citas(self):
        """
        Devuelve la lista de citas almacenadas.
        """
        datos = self._leer_datos()
        return datos["citas"]
    
    def _escribir_datos(self, datos):
        """
        Sobrescribe el archivo JSON con los datos proporcionados.
        """
        with self.ruta_archivo.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

    def guardar_profesional(self, profesional_dict):
        """
        Guarda un profesional en el archivo.
        """
        datos = self._leer_datos()
        datos["profesionales"].append(profesional_dict)
        self._escribir_datos(datos)

    def guardar_cliente(self, cliente_dict):
        """
        Guarda un cliente en el archivo.
        """
        datos = self._leer_datos()
        datos["clientes"].append(cliente_dict)
        self._escribir_datos(datos)

    def guardar_cita(self, cita_dict):
        """
        Guarda una cita en el archivo.
        """
        datos = self._leer_datos()
        datos["citas"].append(cita_dict)
        self._escribir_datos(datos)






