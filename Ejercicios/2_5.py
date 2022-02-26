"""5. Lea dos números, calcule el cociente de dividir el primero por el segundo. 
Imprima el cociente. Pero recuerde que antes de hacer la división debe 
evaluar que el divisor no sea igual a cero (0). Porque en este caso debe
 imprimir 'la división no es posible'
"""

num1 = num2 = 0
div = 0.0

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num2 == 0:
    print("La división no es posible")
else:
    div = num1/num2
    print(f"El resultado de la división es: {div:.2f}")