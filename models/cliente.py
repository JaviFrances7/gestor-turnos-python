class Cliente:
    '''Representa los clientes y valida los datos introducidos'''
    def __init__(self,nombre, edad):
        self.nombre = self.validar_nombre(nombre)
        self.edad = self.validar_edad(edad)

    def validar_nombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser texto")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")

        return nombre.strip()
    
    def validar_edad(self, edad):
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número")

        if edad <= 0:
            raise ValueError("La edad debe ser mayor que cero")

        return (edad)
    
    
        