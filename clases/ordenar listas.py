#hay muchas formas de ordenar listas
listaa = [1,4,8,2,3,21,10]

print(listaa)

for i in range(len(listaa)):
    for j in range(i+1,len(listaa)): #j empezara en el ciclo como i+1, lo que significa que j va a empezar como el sucesor de i
        if listaa[i] > listaa[j]:
            c = listaa[i]
            listaa[i]=listaa[j]
            listaa[j]=c

print(listaa)

