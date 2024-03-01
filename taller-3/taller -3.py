# Programa para calcular el precio de venta de diferentes productos en una papeleria

# Entrada

Precio_Costo = int(input (" Por favor ingrese el precio que le costo el producto : " ) )

# Proceso

if Precio_Costo < 3000:

    GANANCIA = Precio_Costo *0.15

elif Precio_Costo <= 6000:

    GANANCIA = Precio_Costo*0.25
else:
    GANANCIA = 500

PRECIO_VENTA = (GANANCIA + Precio_Costo)
#Salida
print ("el producto adquirido se debe vender a",PRECIO_VENTA,)