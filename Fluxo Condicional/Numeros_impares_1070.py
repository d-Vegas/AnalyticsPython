valor = int(input())

for i in range(6) :   
    if valor % 2 != 0 :
        print(valor)
        valor += 2
    else :
        print(valor + 1)
        valor += 2
