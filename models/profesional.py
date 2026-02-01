class Profesional:
    '''Representa cada profesional y valida los datos introducidos'''
    def __init__(self, nombre, especialidad, horario):
        self.nombre = self.validar_nombre(nombre)
        self.especialidad = self.validar_especialidad(especialidad)
        self.horario = horario

    def validar_nombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser texto")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")

        return nombre.strip()
    
    def validar_especialidad(self, especialidad):
        if not isinstance(especialidad, str):
            raise TypeError("La especialidad debe ser texto")

        
        if not especialidad.strip():
            raise ValueError("La especialidad no puede estar vacia")

        return especialidad.strip()
        