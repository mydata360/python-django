'''
Tres personas deciden invertir su dinero para fundar una empresa. 
Cada una de ellas invierte una cantidad distinta. 
Obtener el porcentaje que cada uno invierte con respecto a 
la cantidad total invertida.
'''
num_inversores = 3;inversion_total = 0
inversores = {};inversores_part = {}

#num_inversores = int(input("Indique el número total de inversores: "))

num_inversores += 1

for i in range(1,num_inversores):
    valor_inversion = int(input(f"Valor a invertir persona {i}: "))
    inversores[f"Inversor {i}"] = valor_inversion

inversores_keys = list(inversores.keys())
inversores_values = list(inversores.values())
inversion_total = sum(inversores_values)

print(f"Inversión total: {inversion_total}")

num_inversores-=1

for i in range(0,num_inversores):
    part_inversion = round((inversores_values[i] / inversion_total)*100,1)
    inversores_part[inversores_keys[i]] = part_inversion

print(f"La participación de cada inversor es: {inversores_part}")
