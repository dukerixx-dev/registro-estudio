#transponer matrices
matriz = [[1,2,3],[4,5,6]]
trps= []

for col in range(len(matriz[0])):
    nueva_fila=[]
    for fila in range(len(matriz)):
       nueva_fila.append(matriz[fila][col])
    trps.append(nueva_fila)    

print("matriz original")

for fila in matriz:
    print(fila)

print("matriz transpuesta")

for fila in trps:
    print(fila)