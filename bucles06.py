intentos = 1
clave = input("Escribe tu clave: ")

while clave != "secreto":
    clave = input("Escribe de nuevo tu clave: ")
    intentos = intentos + 1

print("Ha acertado, sus intentos totales son: ", intentos)