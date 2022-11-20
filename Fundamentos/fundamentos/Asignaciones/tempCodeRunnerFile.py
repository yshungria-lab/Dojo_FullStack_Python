
input_lowNum = int(input("Ingresa el numero menor: "))
input_highNum = int(input("Ingresa el numero mayor: "))
input_mult = int(input("Ingresa el numero multiplo: "))
for x in range(input_lowNum, input_highNum+1, 1):
    if x % input_mult == 0:
        print(x)
