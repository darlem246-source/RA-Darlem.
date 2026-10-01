from estudiante import Estudiante
from curso import Curso
from matricula import Matricula

estudiante = Estudiante("Juan Perez", "12345", 17)

curso = Curso("Desarrollo De Aplicaciones", 4)

matricula = Matricula(estudiante, curso)

print("ESTUDIANTE")
print(estudiante.get_nombre())
print(estudiante.get_codigo())
print(estudiante.get_edad())

print("\nCURSO")
print(curso.get_nombre())
print(curso.get_codigo())

print("\nMATRICULA")
print(matricula.get_estudiante().get_nombre())
print(matricula.get_curso().get_nombre())


print("\n- PRUEBAS -")

print("Estudiante:", estudiante.get_nombre())
print("Curso:", curso.get_nombre())
print("Matricula:", matricula.get_estudiante().get_nombre())

print("\nPrueba completada correctamente.")


print("\nGestion de memoria:")

print("El objeto estudiante está creado en memoria.")
print("El objeto curso está creado en memoria.")
print("El objeto matricula está creado en memoria.")