estudiantes = [("ana",19,6.5,7.0,6.8)]
estudiante1 = estudiantes[0]    #extrae o descomprime solo la tupla en la posicion 0
nom,edad,n1,n2,n3=estudiante1   #solo del estudiante ana
print(edad)

mejorprom = 0
for alumno in estudiantes:      #alumno representa a todos las tuplas de la lista
    nom,_,n1,n2,n3=alumno
    prom=(n1+n2+n3)/3

    if prom > mejorprom:
        mejorprom=prom
        mejoralumno=nom 

    print("el nombre es: "+nom) 
    print("el promedio es: ", prom)

    if edad >= 18:
        print(nom+ " es mayor de edad") 

print(f"el mejor promedio encontrado es de {mejoralumno} : {mejorprom:.2f}")    #.2f  : es la cantidad de decimales que quieres truncar en un float