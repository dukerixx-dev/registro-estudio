#tipo de dato Int (Integer,entero)
a = 2
e = 3
suma = a+e
print(suma)

#Tipo de dato Float (Flotante, reales)
1.0e3      #tambien se pueden anotar numeros en notacion cientifica, "e" es el 10 elevado a

pi = 3.14159
radio = 2.0
area = pi * (radio ** 2)        #resultado: 12.56636
print(area)
#tipo de dato Str (Strings)
letra = "a"
palabra = "pytron"
frase = "hola mundo"

print(letra)    #imprime a
print(palabra)  #imprime pytron
print(frase)    #imprime hola mundo

#caracteres especiales en cadenas
    #python permite usar secuencias de escape dentro de cadenas de texto

    #salto de linea \n              #retroceso \b
    #tabulador \t                   #retorno de carro \r
    #comilla simple \'              #avance de hoja \f
    #comilla doble \                #número octal \ooo
    #barra invertida \\             #número hexadecimal \xhh

#impresión en pantalla
    #python permite dar formato a la salida de varias maneras:

    #concatenación: print("hola"+ nombre)
    #comas: print('edad', edad)
    #f-strings (recomendado): print(f'edad: {edad}')
nombre = "ana"
edad = 20
print(f"Mi nombre es {nombre} y tengo {edad} años")

#lectura desde el teclado: input
    #en python el input siempre devuelve una cadena (str), por lo que hay que convertir al tipo de dato que deseamos
nombre1 = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
altura = float(input("ingrese su altura: "))

print("\nLos datos ingresados fueron:")
print(f"Nombre: {nombre}")
print(f"edad: {edad}")
print(f"Altura: {altura:.2f} m")

