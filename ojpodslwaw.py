palabra="tutancamon67"
print(palabra[3:7])
palabra="HOla"
print( len(palabra))
print( palabra.upper( ) )   #MAYUSCULA
print( palabra.lower( ) )   #minuscula


fila, columna= 3,3
matriz=[]

for i in range(fila):
    lista=[]
    for j in range(columna):
        lista.append(i+j)
    matriz.append(lista)
for fila in matriz:
    print(fila)

dia = int(input("lunes[1], martes[2], miercoles[3], jueves[4], viernes[5], sabado[6], domingo[7]: "))
match dia:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3:
        print("miercoles")
    case 4:
        print("jueves")
    case 5:
        print("viernes")
    case 6:
        print("sabado")
    case 7:
        print("domingo")
    case _:
        print("opcion no valida")

    