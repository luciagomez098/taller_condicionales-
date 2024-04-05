# Programa para saber si los 2 numeros dados son multiplos

# Input


A = int( input (" Ingrese por favor un numero: " ) )

B = int( input ( " Ingrese por favor un numero: " ) )

# Processing y Output

if A%B ==0 or B%A ==0:

    print( " Los numeros",A,"y",B,"son multiplos " )

else:

    print( " Los numeros",A,"y",B,"no son multiplos " )