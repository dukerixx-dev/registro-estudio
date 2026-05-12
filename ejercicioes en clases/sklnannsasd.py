##dos listas y quiero una tercera que solo guarde los elementos comunes (solo ocupando listas)
lista1= [1,4,7,1]
lista2 = [1,1,1,4,5,7]
lista3 = []

for i in range(len(lista1)):
    for j in range(len(lista2)):
        if lista1[i] == lista2[j]:
            flag=0
            #verificando si esta preente en la lista 3
            for k in  range(len(lista3)):
                if lista1[i] == lista3[k]:
                    flag=1
            if flag == 0:
                lista3.append(lista1[i])

           
print(lista3)    



#for k in range(len(lista_nueva)):       #es un paso extra que puede ser innecesario
    #for l in range(k+1,len(lista_nueva)):
        #if lista_nueva[k] == lista_nueva[l]:


        