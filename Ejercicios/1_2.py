#2. Suponga que un individuo desea invertir su capital en un banco 
# y desea saber cuánto dinero ganará después de un mes, si el banco paga a razón de n% mensual.

capital = 0
porcGanancia = 0.0
ganancia = 0.0

capital = int(input("Ingrese el valor a invertir: "))
porcGanancia = float(input("Indique el '%' de ganancia: "))
ganancia = capital * porcGanancia

print(f"La ganacia mensual es: {ganancia}")