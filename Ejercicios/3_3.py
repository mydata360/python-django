"""
3. Un Zoológico pretende determinar el porcentaje de animales que 
hay en las siguientes tres categorías de edades: de 0 a 1 año, de más de 1 año 
y menos de 3 y de 3 o más años. El zoológico todavía no está seguro del animal 
que va a estudiar. Si se decide por elefantes solo tomara una muestra de
 20 de ellos; si se decide por las jirafas, tomara 15 muestras, y si 
 son chimpancés tomara 25.
"""

rango1 = rango2 = rango3 = n = 0
animal = ""

tipo = int(input("Indique el tipo de animal (1:Elefantes, 2:Jirafas, 3:Chimpacés): "))

if tipo == 1:
    n = 20
    animal = "Elefantes"
elif tipo == 2:
    n = 15
    animal = "Jirafas"
elif tipo == 3:
    n = 25
    animal = "Chimpancés"

for i in range(0, n):
    edad = int(input(f"Indique la edad del animal #{i}: "))

    if edad >= 3:
        rango3 += 1
    elif edad == 2:
        rango2 += 1
    elif edad <= 1:
        rango1 +=1

porcRango1 = (rango1 / n) * 100
porcRango2 = (rango2 / n) * 100
porcRango3 = (rango3 / n) * 100

print(f"Tipo animal: {animal}")
print(f"Muestra total: {n}")
print(f"El porcentaje de edad entre 0 y 1 años es: {porcRango1:.1f}%")
print(f"El porcentaje de edad 2 años es: {porcRango2:.1f}%")
print(f"El porcentaje de edad de 3 o más años es: {porcRango3:.1f}%")