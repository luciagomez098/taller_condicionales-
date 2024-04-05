from math import*

# Programa para calcular e imprimir  las raìces de las ecuaciòn de segundo grado de coeficientes reales.

# Imput

a = int(input ( "Por favor ingrese el valor de a: " ) )

b = int(input ( "Por favor ingrese el valor de b: " ) )

c = int(input ( "Por favor ingrese el valor de c: " ) )


# Processing

if a==0 :
    print ( " No se puede realizar la ecuaciòn cuadratica " )

else :
    d = b**2-4*a*c
    if d ==0 :
         x1 = -b/2*a
         x2 = x1
         print ( "Los resultado finales de la ecuaciòn son : " , x1, x2 , )
    elif d > 0 :
        x1 = ( -b + sqrt (d)) /2*a
        x2 = ( -b - sqrt (d)) /2*a
        print ( " Los resultados finales de la ecuaciòn son :" , x1 , x2 , )
    else :
        print ( "No se puede realizar la ecuaciòn " )