inicio = int(input(" Digite o numero de inicio: "))
fim  = int(input(" Digite o numero para terminar: "))

soma = 0

for n in range(inicio, fim, 1):
    if n % 2 == 0:
        soma += n

else:
        if soma == 0:
            print(" Não há um numero par no intervalo. ")
        else:
            print(f" A soma dos é {soma}")