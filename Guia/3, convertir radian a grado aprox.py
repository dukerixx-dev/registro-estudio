#convertir radianes a grados redondeando a un decimal
import math     #importamos una de la librerias de la cual contiene el numero pi

radian = int(input("ingrese los radianes "))     #un radian es el angulo que se da cuando el radio y la longitud de un segmento del circulo son iguales
grados = radian * (180/math.pi)                 #un grado es una parte de las 360 que se divide el circulo (aunque no sé del por qué)

print(f"{radian} radianes a grados son {round(grados,1)}°")
