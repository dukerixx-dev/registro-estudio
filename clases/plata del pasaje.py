#ingresar una cantidad  y restarlo con los pasajes del bus
plata = int(input(f"ingrese la plata que tendrá para el pasaje: "))

print("escenario 1: pagar estudiante en bus y completo en micro")
print("pasaje_bus = 1500")
pasaje_bus = 1500
print("pasaje_micro = 800")
pasaje_micro = 800
ida_y_vuelta =(pasaje_bus + pasaje_micro)*2
print(f"por lo que la ida y vuelta seran de: {ida_y_vuelta} y menos la plata ingresa será de {plata - ida_y_vuelta}")
print(f"y esto por 4 dias quedarían {plata - (ida_y_vuelta)*4 }\n")

print("escenario 2: pagar estudiante completo")
print("pasaje_bus = 1500")
pasaje_bus = 1500
print("pasaje_micro = 260")
pasaje_micro = 260
ida_y_vuelta =(pasaje_bus + pasaje_micro)*2
print(f"por lo que la ida y vuelta seran de: {ida_y_vuelta} y menos la plata ingresa será de {plata - ida_y_vuelta}")
print(f"y esto por 4 dias quedarían {plata - (ida_y_vuelta)*4 }\n")

print("escenario 3: pagar estudiante en bus y una sola vez en micro")
print("pasaje_bus = 1500")
pasaje_bus = 1500
print("pasaje_micro = 260 + 800")
pasaje_micro = 260 + 800
ida_y_vuelta = pasaje_bus *2 + pasaje_micro
print(f"por lo que la ida y vuelta seran de: {ida_y_vuelta} y menos la plata ingresa será de {plata - ida_y_vuelta}")
print(f"y esto por 4 dias quedarían {plata - (ida_y_vuelta*4)}")
