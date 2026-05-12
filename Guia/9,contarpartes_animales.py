vacas=int(input("ingrese la cantidad de vacas: "))
pollos=int(input("ingrese la cantidad de pollos: "))
cerdos=int(input("ingrese la cantidad de cerdos: "))

cabezas=vacas+pollos+cerdos
patas= 4*vacas + 2*pollos + 4*cerdos

print(f"en la granja en total hay {cabezas} cabezas y {patas} patas")