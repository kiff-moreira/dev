numero = []


for n in range(6):
    num = int(input(f' Digite o {n+1}º numero: '))
    numero.append(num)

soma = sum(numero)

print(f' A soma dos numeros digitados é {soma}')
