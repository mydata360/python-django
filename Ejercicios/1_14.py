'''
Un alumno desea saber cuál será su promedio general en las tres materias 
más difíciles que cursa y cuál será el promedio que obtendrá en cada una de ellas. 
Estas materias se evalúan como se muestra a continuación:
La calificación de Matemáticas se obtiene de la sig. manera:
• Examen 90%
• Promedio de tareas 10%
• En esta materia se pidió un total de tres tareas.
La calificación de Física se obtiene de la sig. manera:
• Examen 80%
• Promedio de tareas 20%
• En esta materia se pidió un total de dos tareas.
La calificación de Química se obtiene de la sig. manera:
• Examen 85%
• Promedio de tareas 15%
• En esta materia se pidió un promedio de tres tareas.
'''
valores_examenes = {}
tareas = {}
valores_tareas = []
promedios_tareas = {}

materias = {'matematicas':{'examen':0.9,'tareas':0.1,'num_tareas':3},\
            'fisica':{'examen':0.8,'tareas':0.2,'num_tareas':2},\
            'quimica':{'examen':0.8,'tareas':0.2,'num_tareas':3}}

materias_keys = list(materias.keys())
num_materias = len(materias_keys)

for i in range(0,num_materias):
    materia = materias_keys[i]
    valor_examen = float(input(f'Indique calificación exámen para {materia}: '))
    valores_examenes[materia] =  valor_examen        
    
    num_tareas = materias[materia]['num_tareas']
    print(f'Tareas para {materia}: {num_tareas}')

    num_tareas +=1
    for j in range(1,num_tareas):
        tarea = f'tarea {j}'
        valor_tarea = float(input(f'Indique calificación para {materia} {tarea}: '))
        valores_tareas.append(valor_tarea)
    tareas[materia] = list(valores_tareas)
    valores_tareas.clear()     
    promedio_tareas = sum(valores_tareas) / len(valores_tareas)
    promedios_tareas[materia] = promedio_tareas

print(valores_examenes)
print(tareas)







