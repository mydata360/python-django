"""
7. Dada una cantidad en pesos, obtener la equivalencia en dólares, 
asumiendo que la unidad cambiaría es un dato desconocido.
"""

TRM = valorCOP = valorUSD = 0.0

valorCOP = float(input("Ingrese el valor en pesos Colombianos (COP): "))
TRM = float(input("Indique el valor de la TRM de hoy: "))

valorUSD = valorCOP / TRM

print(f"La equivalencia en dólares (USD) es: {valorUSD:.2f}")