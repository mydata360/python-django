#3. Un vendedor recibe un sueldo base más un 10% extra por comisión 
# de sus ventas, el vendedor desea saber cuánto dinero obtendrá por 
# concepto de comisiones por las tres ventas que realiza en el mes y 
# el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo = 0
porcComision = 0.1

venta1 = int(input("Ingrese al venta 1: "))
venta2 = int(input("Ingrese al venta 2: "))
venta3 = int(input("Ingrese al venta 3: "))

ventaTotal = venta1 + venta2 + venta3

sueldo = int(input("Ingrese el sueldo: "))
comision = ventaTotal * porcComision

sueldoTotal = sueldo + comision

print(f"La venta total del mes es: {ventaTotal}")
print(f"La comisión total es: {comision}")
print(f"El total a recibir es: {sueldoTotal}")