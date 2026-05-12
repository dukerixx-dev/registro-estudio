#pedir 5 numeros y contar cuantos son positivos
cont = 0
num1 = int(input("ingrese un numero"))
if num1 > 0:
    cont +=1
num2 = int(input("ingrese otro numero"))
if num2 > 0:
    cont +=1
num3 = int(input("ingrese otro numero"))
if num3 > 0:
    cont +=1
num4 = int(input("ingrese otro numero"))
if num4 > 0:
    cont +=1
num5 = int(input("ingrese otro numero"))
if num1 > 0:
    cont +=1
print(f"Hay {cont} numeros positivos en los numeros ingresados")
