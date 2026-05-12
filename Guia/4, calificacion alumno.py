#segun la calificacion ingresada indicar si aprueba o rinde el examen el alumno,
# si rinde el examen este tendra un 30% de ponderacion, para aprobar es arriba de un 4.0 .
nota = float(input("ingrese la clasificación del alumno: "))



if nota >= 4.0:
    print("el alumno aprobó")
else:
    print("el alumno no aprobó, puede rendir el remedial")
    remedial = float(input("ingrese la calificación que tuvo el alumno en el remedial: "))
    nota = nota*0.7 + remedial*0.3
    print(f"el alumno sacó: {round(nota,1)}")
    if nota >= 4.0:
        print("el alumno aprobó")
    else:
        print("el alumno no aprobó")
