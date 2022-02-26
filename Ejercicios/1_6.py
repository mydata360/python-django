"""
6. Un maestro desea saber qué porcentaje de hombres y que porcentaje de 
mujeres hay en un grupo de n estudiantes.
"""

total = hombres = mujeres = 0
genero = ""
porcH = porcM = 0.0

total = int(input("Indique el total de estudiantes: "))

for i in range(0, total):
    genero = input(f"Indique el género del estudiante # {i} (M: Masculino, F:Femenino): ")

    if genero == "M":
        hombres += 1
    elif genero == "F":
        mujeres += 1

porcH = (hombres / total) * 100
porcM = (mujeres / total) * 100

print(f"Total de estudiantes: {total}")
print(f"El porcentaje de hombres es: {porcH:.1f}%")
print(f"El porcentaje de mujueres es: {porcM:.1f}%")