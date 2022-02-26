'''
Calcular el nuevo salario de un empleado, 
sabiendo que se tuvo un incremento del 25% sobre su salario anterior.
'''
salario = 0
por_incremento = 0.25
salarioFinal = 0

salario = int(input("Indique el valor del salario: "))
incremento = salario * por_incremento
salarioFinal = salario + incremento

print(f"El valor del salario con descuento es: $ {salarioFinal}")