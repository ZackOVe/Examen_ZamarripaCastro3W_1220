print("")
print("Zamarripa Castro Erick Fabian 3W 1220")
print("")

#Pide al usuario las materias
asig1 = input(str("Ingrese la primera asignatura: "))
asig2 = input(str("Ingrese la segunda asignatura: "))
asig3 = input(str("Ingrese la tercera asignatura: "))
asig4 = input(str("Ingrese la cuarta asignatura: "))
asig5 = input(str("Ingrese la quinta asignatura: "))

print(" ")

#Junta las 4 variables en una lista
Asignaturas=[asig1, asig2, asig3, asig4, asig5]
#imprime la lista
print(Asignaturas)

print(" ")

#Pide al usuario las calificaciones
calif1=float(input("Ingrese su calificacion de la primera "))
calif2=float(input("Ingrese su calificacion de la segunda "))
calif3=float(input("Ingrese su calificacion de la tercera "))
calif4=float(input("Ingrese su calificacion de la cuarta "))
calif5=float(input("Ingrese su calificacion de la quinta "))
print(" ")

#Junta todo para el final
calif=[calif1, calif2, calif3, calif4, calif5]
print(calif)
print(" ")

#Imprime el resultado
print("En la materia ",Asignaturas[0], " tienes  ", calif[0])
print("En la materia ",Asignaturas[1], " tienes  ", calif[1])
print("En la materia ",Asignaturas[2], " tienes  ", calif[2])
print("En la materia ",Asignaturas[3], " tienes  ", calif[3])
print("En la materia ",Asignaturas[4], " tienes  ", calif[4])

#Verifica y luego imprime para al final eliminar las aprobadas
if calif1<= 5:
    print("Reprobo", Asignaturas[0])
    print("Debe repetirla")
    print(" ")

if calif2<= 5:
    print("Reprobo", Asignaturas[1])
    print("Debe repetirla")
    print(" ")

if calif3<= 5:
    print("Reprobo", Asignaturas[2])
    print("Debe repetirla")
    print(" ")

if calif4<= 5:
    print("Reprobo", Asignaturas[3])
    print("Debe repetirla")
    print(" ")

if calif5<= 5:
    print("Reprobo", Asignaturas[4])
    print("Debe repetirla")
    print(" ")

print(asig3, "Sera removida de la lista")

Asignaturas.remove(asig3)
print(Asignaturas)