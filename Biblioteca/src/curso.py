class Curso:

    def __init__(self, nombre, codigo):

        if nombre == "":
            raise ValueError("El nombre del curso no puede estar vacío.")

        if codigo == "":
            raise ValueError("El código del curso no puede estar vacío.")

        self.__nombre = nombre
        self.__codigo = codigo

    def get_nombre(self):
        return self.__nombre

    def get_codigo(self):
        return self.__codigo