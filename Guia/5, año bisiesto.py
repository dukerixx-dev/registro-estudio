año=int(input("ingrese el año que quiere revisar si es bisiesto: "))
multiplo_4 = año%4
multiplo_100 = año%100

#hacer un ciclo que evalue los multiplos de 4, 10 y de los dos juntos hasta que llegue al año que eligio el usario

if año%4 == 0:
    if año%100 == 0:
        if año%400 == 0:
            print(f"el año {año} es bisiesto") 
        else:
            print(f"el año {año} No es bisiesto")
    else:
        print(f"el año {año} es bisiesto") 
else:
    print(f"el año {año} No es bisiesto")


#pipipipiipipipippipiipipiippiipipipipipi
