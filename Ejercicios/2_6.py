"""
6. Para un salario bruto hasta de $ 250.500 no hay retención. 
Para un salario bruto de $ 250.501 a $ 300.000 el porcentaje de 
retención es de 5%. para un salario bruto mayor a $300.000 el 
porcentaje de retención es del 8%. Imprimir el nombre del empleado, 
el salario bruto, el valor de la retención y el salario neto 
(salario bruto menos la retención).

"""

porcRet = salarioBruto = valorRet = salarioNeto = 0.0
empleado = ""

empleado = input("Ingrese el nombre del empleado: ")
salarioBruto = float(input("Ingrese el salario bruto: "))

if salarioBruto > 300000:
    porcRet = 0.08
elif salarioBruto >= 250501:
    porcRet = 0.05
else:
    porcRet = 0

valorRet = salarioBruto * porcRet
salarioNeto = salarioBruto - valorRet

print(f"Nombre del empleado: {empleado}")
print(f"Salario bruto: {salarioBruto}")
print(f"Valor retención: {valorRet}")
print(f"Salario neto: {salarioNeto}")