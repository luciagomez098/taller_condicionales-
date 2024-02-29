# Programa para calcular en que cuadrante esta un punto,de un plano cartesiano

# Entrada
X = int(input("ingrese la coordenada x: "))
Y = int(input("ingrese la coordenada y: "))

# Proceso
if X == 0:
    if Y == 0:
        print("la coordenada" , (X, Y),"esta en el origen del plano cartesiano(0,0)")
    else:
        print("la coordenada" , (X, Y),"estas en el eje Y")
elif Y == 0:
    print("la coordenada" , (X, Y),"estas en el eje X")
elif X > 0:
    if Y > 0:
        print("la coordenada" , (X, Y),"estas en el cuadrante 1")
    else:
        print("la coordenada" , (X, Y),"estas en el cuadrante 4")
elif Y < 0:
    print("la coordenada" , (X, Y),"estas en el cuadrante 3")
else:
    print("la coordenada" , (X, Y),"estas en el cuadrante 2")

