#ingresar 3 numeros, utilizando condiciones indicar cual es el orden de menor a mayor
nums = []
for j in range(3):
    n= int(input("ingrese un numero "))
    nums.append(n)
if nums[0] > nums[1] > nums[2]:
   print(f"el orden de menor a meyor de los numeros ingresados son: {nums[2]}, {nums[1]} y {nums[0]}")
else :
    if nums[0] > nums[2] > nums[1]:
        print(f"el orden de menor a meyor de los numeros ingresados son: {nums[1]}, {nums[2]} y {nums[0]}")
    else :
        if nums[1] > nums[0] > nums[2]:
            print(f"el orden de menor a meyor de los numeros ingresados son: {nums[2]}, {nums[0]} y {nums[1]}")
        else:
            if nums[1] > nums[2] > nums[0]:
                print(f"el orden de menor a meyor de los numeros ingresados son: {nums[0]}, {nums[2]} y {nums[1]}")
            else:
                if nums[2] > nums[1] > nums[0]:
                    print(f"el orden de menor a meyor de los numeros ingresados son: {nums[0]}, {nums[1]} y {nums[2]}")
                else: 
                    print(f"el orden de menor a meyor de los numeros ingresados son: {nums[1]}, {nums[0]} y {nums[2]}")