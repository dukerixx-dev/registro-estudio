#ciclos

#Proposicion while
    #el bucle while en python es una estructura de control que repite un bloque de codigo mientras una condicion se mantenga verdadera
    #
    #la expresion condicional 

#ciclos for
    #la funcoin range() genera una secuencia de números que se puede recorrer un bucle FOR. es muy utilizada cuando se desea repetir un bloque de código una cantidad especifica de vece
    # sintaxix:
    #range(fin): desde 0 hasta fin - 1
    #range(inicio,fin): desde inicio hasta fin - 1
    #range(inicio,fin,paso): con incremento o decremento

for i in range (1, 8):
    for j in range (1, i + 1):
          print("*", end= "1")
    print()
    
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

#preposicion match-case