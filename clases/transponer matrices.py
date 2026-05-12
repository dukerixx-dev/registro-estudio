#transponer matrices
matris1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
matris2 = []
print(matris1)

for j in range(len(matris1[0])):
    lista = []
    for i in range(len(matris1)):
        lista.append(matris1[i][j]) 
    matris2.append(lista)    
print(matris2)

for fila in matris1:    #la palabra "fila" y "col" los interpreta como eso de las matrices
    print(fila)

for fila in matris2:
    print(fila)




