#1 Calcule el área del triángulo y muestre su resultado

altura = base = 0
area = 0.0

altura = int(input("Ingrese la altura del triángulo: "))
base = int(input("Ingrese la base del triángulo: "))

area = (base * altura) / 2

print(f"El área del triángulo es: {area:.1f}")
