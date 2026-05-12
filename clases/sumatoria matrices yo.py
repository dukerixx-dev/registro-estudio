#sumatoria  de matrices

matriz1 = [[1,2],[3,4]]
matriz2 = [[5,6],[7,8]]
matriz_suma = []

for i in range(len(matriz1)):
    lista=[]
    for j in range(len(matriz1[i])):
        lista.append(matriz1[i][j] + matriz2[i][j])
    matriz_suma.append(lista)


print(matriz_suma)      #falto transformarlo en una matris