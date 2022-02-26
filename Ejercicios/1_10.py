'''
En un hospital existen tres áreas: Ginecología, Pediatría, 
Traumatología. El presupuesto anual del hospital se reparte 
conforme a la sig. tabla:

Área Porcentaje del presupuesto
Ginecología 40%
Traumatología 30%
Pediatría 30%

Obtener la cantidad de dinero que recibirá cada área, 
para cualquier monto presupuestal.
'''

presupuesto = 0
areas = {'gineco':0.4,'trauma':0.3,'pediatria':0.3}
areas_keys = list(areas.keys())
areas_values = list(areas.values())

presupuesto = int(input("Indique el presupuest del periodo: "))

num_areas = len(areas)
presupuesto_areas = {}

for i in range(0,num_areas):
    presupuesto_areas[areas_keys[i]] = presupuesto*areas_values[i]

print(f"Los presupuestos para cada área son: {presupuesto_areas}")