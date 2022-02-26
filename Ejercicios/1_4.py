#4. Una tienda ofrece un descuento del 15% sobre el total de la compra y 
# un cliente desea saber cuánto deberá pagar finalmente por su compra.

valorCompra = 0
porcDescuento = 0.15

valorCompra = int(input("Indique el valor de la compra: "))

descuento = valorCompra * porcDescuento
valorPago = valorCompra-descuento

print(f"Descuento: {descuento}")
print(f"valorPago: {valorPago:.1f}")