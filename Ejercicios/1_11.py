'''
El dueño de una tienda compra un artículo a un precio 
determinado. Obtener el precio en que lo debe vender 
para lograr una ganancia del 30%.
'''
precio_compra = 0; precio_venta = 0; por_ganancia = 0.3; ganancia = 0.0

precio_compra = int(input("Indique el precio de compra: "))
ganancia = precio_compra * por_ganancia
precio_venta = precio_compra + ganancia

print(f"El precio de venta para un 30% de ganancia es: {precio_venta}")