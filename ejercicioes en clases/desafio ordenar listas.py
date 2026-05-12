#dos listas y quiero una tercera que solo guarde los elementos comunes (solo ocupando listas)
lista1=[1,7,9,9,9,9,7]
lista2=[1,7,9]      #haerlo como los reactivos excesivo y limitantes de quimica (insano)
lista_nueva=[]

dif_listas = abs(len(lista1) - len(lista2))      #busco la diferencia en el largo entre las dos listas

if len(lista1) > len(lista2):                    #si una lista es mayor a otra le resto a esta la diferencia obtenida anteriormente
    len_limitante = len(lista1) - dif_listas   #para obtener largo de la lista menor, que usaremos para definir el largo maximo de la lista nueva
    len_exceso = len(lista1)
    lista_limitante = lista2
    lista_exceso = lista1
else:
    len_limitante = len(lista2) - dif_listas   #si no se cumple, se hara lo mismo lo contrario, y si son iguales la diferencia será 0 asi que no habra cambios
    len_exceso = len(lista2)
    lista_limitante = lista1
    lista_exceso = lista2

for i in range(len_limitante):                 #se establece el largo maximo de la lista nueva
    for j in range(len_exceso):
        if i == (len_limitante-1)  and j > (len_limitante - 1):
            break
        if lista_limitante[i] == lista_exceso[j]:
            lista_nueva.append(lista_limitante[i])      
    
print("lista nueva:")
print(lista_nueva)