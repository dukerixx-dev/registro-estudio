#multiplicar matrices
matrizA = [[1,2,3],[4,5,6]]
matrizB = [[7,8],[9,10],[11,12]]
matriz_nueva=[]
sumatoria=0

for k in range(len(matrizB[0])):
    lista = []
    for i in range(len(matrizA)):
        sumatoria=0
        for j in range(len(matrizB)):
            sumatoria = (matrizA[k][j]*matrizB[j][i]) + sumatoria
        lista.append(sumatoria)
    matriz_nueva.append(lista)    

print (matriz_nueva)