class Estudiante:

    def __init__(self, nombre, codigo, edad):

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío.")

        if codigo == "":
            raise ValueError("El código no puede estar vacío.")

        if edad <= 0:
            raise ValueError("La edad debe ser mayor que 0.")

        self.__nombre = nombre
        self.__codigo = codigo
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_codigo(self):
        return self.__codigo

    def get_edad(self):
        return self.__edad