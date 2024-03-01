# Programa para calcular el precio de venta de diferentes productos en una papeleria

# Entrada

Precio_Costo = int(input (" Por favor ingrese el precio que le costo el producto : " ) )

# Proceso

if Precio_Costo < 3000:

    GANANCIA = Precio_Costo*0.15

elif Precio_Costo <= 6000:

    GANANCIA = Precio_Costo *500
else:
    GANANCIA = Precio_Costo *0.25 
PRECIO_VENTA = (GANANCIA + Precio_Costo)
#Salida
print ("el producto adquirido se debe vender a",PRECIO_VENTA,)