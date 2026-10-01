class Matricula:

    def __init__(self, estudiante, curso):

        if estudiante is None:
            raise ValueError("Debe existir un estudiante.")

        if curso is None:
            raise ValueError("Debe existir un curso.")

        self.__estudiante = estudiante
        self.__curso = curso

    def get_estudiante(self):
        return self.__estudiante

    def get_curso(self):
        return self.__curso