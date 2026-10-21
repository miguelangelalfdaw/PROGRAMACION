nota = float(input("Introduce tu nota: "))
if nota >= 0 and nota <= 10:
    print("Error: Introduce una nota entre 0 y 10")
elif nota < 5:
    print("Suspenso")
elif nota <= 7:
    print("¡Aprobado!")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")

