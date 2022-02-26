'''
Un alumno desea saber cuál será su promedio general en 
la materia algoritmos sabiendo que en total son cuatro 
notas las que se computan
'''
num_notas = 4; notas = {}; nota = 0.0;promedio = 0.0
num_notas+=1

for i in range(1,num_notas):
    nota = float(input(f"Indique la nota {i}: "))
    notas[f'Nota {i}'] = nota

promedio = sum(notas.values()) / len(notas)

print(f"El promedio de las notas es: {promedio:.1f}")
