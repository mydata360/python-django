"""
5. Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.
Dicha calificación se compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final.
"""
c1 = c2 = c3 = promParciales = examenFinal = trabajoFinal = resultadoFinal = 0.0

c1 = int(input("Ingrese calificación parcial 1: "))
c2 = int(input("Ingrese calificación parcial 2: "))
c3 = int(input("Ingrese calificación parcial 3: "))

promParciales = (c1 + c2 + c3) / 3

examenFinal = int(input("Ingrese calificación examen final: "))
trabajoFinal = int(input("Ingrese calificación trabajo final: "))

resultadoFinal = promParciales*0.55 + examenFinal * 0.3 + trabajoFinal*0.15

print(f"La calificacion final es: {resultadoFinal}")