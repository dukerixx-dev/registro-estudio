#ingresar 3 numeros
Nums=[]
for i in range(3):
    num = int(input("ingrese 3 numeros "))  #uso una lista vacia para luego con append ir llenandolo con los numeros q ingresa el usuario
    Nums.append(num)
print(Nums)
#necesitamos conocer que numero es mayor al otro
if Nums[0] > Nums[1]:
    posi_mayor = Nums[0]    #[1]<[0]
    posi_menor = Nums[1]
else:
    posi_mayor = Nums[1]    #[0]<[1]
    posi_menor = Nums[0]
if Nums[2] > posi_mayor:    #([1]<[0] o [0]<[1]) < Nums[2]
    print(f"los numeros ingresados de menor a mayor son: {posi_menor}, {posi_mayor}, {Nums[2]}")
else:
    if Nums[2] > posi_menor:    #quedara en medio: posi_menor < Nums[2] < posi_mayor
        print(f"los numeros ingresados de menor a mayor son: {posi_menor}, {Nums[2]}, {posi_mayor}, ")
    else:   #sino, será el menor de todos
        print(f"los numeros ingresados de menor a mayor son:  {Nums[2]}, {posi_menor}, {posi_mayor}, ")