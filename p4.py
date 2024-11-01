print("")
print("Zamarripa Castro Erick Fabián 3w 1220")
print("")

#Creacion de diccionario
datos = {
    'nombre': ' ',
    'edad': ' ',
    'direccion': ' ',
    'telefono': ' '
}

#El usuario debe introducir sus datos
datos ['nombre'] = str(input("Introduzca su nombre completo empezando por apellido paterno: "))
print ("")
datos['edad'] = str(input("Introduzca su edad: "))
print ("")
datos['direccion'] = str(input("Introduzca direccion: "))
print ("")
datos['telefono'] = str(input("Introduzca numero de telefono: "))
print ("")

#Imprimira los datos
print (datos['nombre'])
print ("")
print ("Tiene:")
print (datos['edad'])
print ("")
print ("Vive en:")
print (datos['direccion'])
print ("")
print ("Su numero es:")
print (datos['telefono'])
print ("")
